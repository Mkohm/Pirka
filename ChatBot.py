import json
import netifaces as network_interfaces
import os
from threading import Thread
from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from database import DatabaseConnector
from database import DatabaseExtractor
from database import DatabaseInserter
from scraper import LoginHandler
from scraper.ItsLearningScraper import ItsLearningScraper
from scraper.BlackboardScraper import BlackboardScraper

# Flask app should start in global layout
app = Flask(__name__)

network_interfaces.ifaddresses('en0')
ip = network_interfaces.ifaddresses('en0')[2][0]['addr']
print("my ip address is: ", ip)

# Holds the current state of the login
validLogin = False

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 8080))


def process_actions(parameter: str, action_name: str) -> str:
    """
    Explanation of parameters
    :param parameter:
    :param action_name:
    :return:
    """
    if action_name == "login":
        return create_followup_event_data(parameter)
    elif action_name == "get_exam_date":
        return create_data_response(DatabaseExtractor.get_exam_date(parameter[1]))
    elif action_name == "get_assessment_form":
        return create_data_response(DatabaseExtractor.get_assessment_form(parameter[1]))
    elif action_name == "get_contact_mail":
        return create_data_response(DatabaseExtractor.get_contact_mail(parameter[1]))
    elif action_name == "get_contact_name":
        return create_data_response(DatabaseExtractor.get_contact_name(parameter[1]))
    elif action_name == "get_contact_phone":
        return create_data_response(DatabaseExtractor.get_contact_phone(parameter[1]))
    elif action_name == "get_contact_website":
        return create_data_response(DatabaseExtractor.get_contact_website(parameter[1]))
    elif action_name == "get_office":
        return create_data_response(DatabaseExtractor.get_contact_office(parameter[1]))
    elif action_name == "get_teaching_form":
        return create_data_response(DatabaseExtractor.get_teaching_form(parameter[1]))
    elif action_name == "get_course_name":
        return create_data_response(DatabaseExtractor.get_course_name(parameter[1]))
    elif action_name == "get_credit":
        return create_data_response(DatabaseExtractor.get_credit(parameter[1]))
    elif action_name == "get_url":
        return create_data_response(DatabaseExtractor.get_url(parameter[1]))
    elif action_name == "get_prereq_knowledge":
        return create_data_response(DatabaseExtractor.get_prereq_knowledge(parameter[1]))
    elif action_name == "get_course_content":
        return create_data_response(DatabaseExtractor.get_course_content(parameter[1]))
    elif action_name == "get_course_material":
        return create_data_response(DatabaseExtractor.get_course_material(parameter[1]))
    elif action_name == "get_teaching_form":
        return create_data_response(DatabaseExtractor.get_teaching_form(parameter[1]))
    # personal:
    elif action_name == "get_exercise_status":
        return create_data_response(DatabaseExtractor.get_exercise_status(parameter[1], parameter[0]))
    elif action_name == "get_project_status":
        return create_data_response(DatabaseExtractor.get_project_status(parameter[1], parameter[0]))
    elif action_name == "get_lab_status":
        return create_data_response(DatabaseExtractor.get_lab_status(parameter[1], parameter[0]))
    elif action_name == "get_next_event":
        return create_data_response(DatabaseExtractor.get_next_event(username=parameter[0]))
    elif action_name == "get_next_assignment":
        return create_data_response(DatabaseExtractor.get_next_assignment(username=parameter[0]))
    elif action_name == "get_this_weeks_schedule":
        return create_data_response(DatabaseExtractor.get_this_weeks_schedule(username=parameter[0]))
    elif action_name == "get_exam_dates":
        return create_data_response(DatabaseExtractor.get_exam_dates(username=parameter[0]))
    elif action_name == "get_days_until_first_exam":
        return create_data_response(DatabaseExtractor.get_days_until_first_exam(username=parameter[0]))
    elif action_name == "get_course_codes":
        return create_data_response(DatabaseExtractor.get_course_codes(username=parameter[0]))
    elif action_name == "get_course_names":
        return create_data_response(DatabaseExtractor.get_course_names(username=parameter[0]))
    elif action_name == "get_number_of_courses":
        return create_data_response(DatabaseExtractor.get_number_of_courses(username=parameter[0]))
    else:
        return "I didn't understand anything, you probably broke me :("


def create_data_response(speech: str) -> str:
    data = {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "Pirka-chatbot-webserver"
    }
    return data


def create_followup_event_data(parameter_value: str):
    data = {
        "followupEvent": {
            "name": "custom_event",
            "data": {
                "user_id": parameter_value,
                "ip_address": ip
            }
        }
    }

    print(json.dumps(data, indent=4))

    return data


def add_ime_api_data():
    file = open("/Users/mariuskohmann/PycharmProjects/Pirka/imeapi/course_codes.txt")
    for line in file:
        course = line.split(",")

        for element in course:
            if "\"code" in element:
                course_code = element.split(":")[1].replace("\"", "")
                if "\\" in course_code or "{" in course_code:
                    continue
                print(course_code)
                DatabaseInserter.add_subject_data(course_code)


def thread_function(username: str, password: str):
    """
    This function runs when the user has logged in. It adds the data that is relevant for this user in its own thread.

    It first add all the user specific data to the database, and then it adds all the IME-API data.

    """



    # Scrapes for additional data that is user specific
    itslearning_scraper = ItsLearningScraper(username, password)
    blackboad_scraper = BlackboardScraper(username, password)

    # adds user-course relation to database
    itslearning_scraper.get_course_list()
    blackboad_scraper.get_course_list()


    # adds user's associated assignment data
    itslearning_scraper.get_all_assignments()
    blackboad_scraper.get_all_assignments()

    #Adding a dummy-object
    DatabaseInserter.add_user_has_course(username=username, course_code="DUMMYCOURSE")

def valid_login(username: str, password: str):
    print("starter valid login")

    try:
        LoginHandler.login(username, password)
        print("setter til true")
        global validLogin
        validLogin = True
    except:
        print("setter til false")
        validLogin = False



"""
All web endpoint functions is listed below
"""

@app.route('/', methods=['POST'])
def webhook():
    json_request = request.get_json(silent=True, force=True)


    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")

    # Then get the parameters and action_name of the result
    parameters = result.get("parameters")

    action_name = result.get("action")

    # Handles different parameters to the process-actions method
    # todo: This method should be fixed better
    if action_name == "login":

        # Depending on if the event "WELCOME_FACEBOOK" or if the user typed "login, get started ect" the
        # resulting json request is different, hence we get the parameter in different ways
        if len(result.get("contexts")) > 1:
            parameter = result.get("contexts")[1].get("parameters").get("facebook_sender_id")
        else:
            parameter = result.get("contexts")[0].get("parameters").get("facebook_sender_id")
    else:
        facebook_id = ""
        if len(result.get("contexts")) > 1:
            facebook_id = result.get("contexts")[1].get("parameters").get("facebook_sender_id")
        elif len(result.get("contexts")) == 0:
            facebook_id = json_request.get("originalRequest").get("data").get("sender").get("id")
        else:
            facebook_id = result.get("contexts")[0].get("parameters").get("facebook_sender_id")

        username = DatabaseConnector.get_values("Select username from user where facebook_id = \"" + facebook_id + "\"")[0][0]

        course_code = parameters.get("course_code")
        parameter = [username, course_code]

    print("process actions, parameter:" + str(parameter[1]) + " actioname: " + action_name)
    speech = process_actions(parameter, action_name)

    response = json.dumps(speech, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response


@app.route('/favicon.ico', methods=['GET'])
def scrape_data_from_last_user():
    users = DatabaseExtractor.get_users()
    lastUsername = users[len(users) - 1][0]
    lastPassword = users[len(users) - 1][1]

    thread = Thread(target=thread_function(lastUsername, lastPassword))
    thread.start()

    return render_template("login_success.html")


@app.route('/login/<current_sender_id>', methods=['POST', 'GET'])
def login(current_sender_id):
    """
    This method handles the login so we can get user information to the blackboard scraper.
    We load a template so the user can login and send us the email and password.
    :return:
    """
    print("login")

    error = None
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]

        print(username, password)

        thread = Thread(target=valid_login(username, password))
        thread.start()
        thread.join()

        global validLogin

        if validLogin:
            DatabaseInserter.add_user(username, password, current_sender_id)
            validLogin = False
            return render_template("login_success.html")
        else:
            return render_template('login.html')

    return render_template('login.html')

    # the code below is executed if the request method
    # was GET or the credentials were invalid


"""
Start app
"""

if __name__ == '__main__':
    # Add all the IME-API data to the database

    #add_ime_api_data()

    app.run(debug=True, host='', port=port, threaded=True)  # Receives action-name, gets the data and returns a string ready to send back to API.AI