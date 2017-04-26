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

# Holds the current state of the login
validLogin = False

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 8080))


def process_actions(parameter: str, action_name: str) -> str:
    """
    This method creates a response to API.AI according to which parameters that was passed by API.AI
    :param parameter: parameter[0] is username, parameter[1] is course_code, parameter[2] is facebook-id
    :param action_name: the action being called in API.AI
    :return: Json - data containing the string that should be returned to the user
    """

    try:
        if action_name == "login":
            return create_followup_event_data(parameter[2])
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
        elif action_name == "get_exercise_status":
            return create_data_response(DatabaseExtractor.get_exercise_status(parameter[1], parameter[0]))
        elif action_name=="get_exercise_scheme_approval":
            return create_data_response(DatabaseExtractor.get_exercise_scheme_approval(parameter[1], parameter[0]))
        elif action_name=="get_exercises_left":
            return create_data_response(DatabaseExtractor.get_exercises_left(parameter[1], parameter[0]))
        elif action_name == "get_next_event":
            return create_data_response(DatabaseExtractor.get_next_event(username=parameter[0]))
        elif action_name == "get_next_assignment":
            return create_data_response(DatabaseExtractor.get_next_assignment(username=parameter[0]))
        elif action_name == "get_this_weeks_schedule":
            return create_data_response(DatabaseExtractor.get_this_week_schedule(username=parameter[0]))
        elif action_name == "get_next_weeks_schedule":
            return create_data_response(DatabaseExtractor.get_next_week_schedule(username=parameter[0]))
        elif action_name == "get_next_weeks_events":
            return create_data_response(DatabaseExtractor.get_next_weeks_events(username=parameter[0]))
        elif action_name == "get_next_weeks_assignments":
            return create_data_response(DatabaseExtractor.get_next_weeks_assignments(username=parameter[0]))
        elif action_name == "get_this_weeks_assignments":
            return create_data_response(DatabaseExtractor.get_this_weeks_assignments(username=parameter[0]))
        elif action_name == "get_this_weeks_events":
            return create_data_response(DatabaseExtractor.get_this_weeks_events(username=parameter[0]))
        elif action_name == "get_passed_assignments":
            return create_data_response(DatabaseExtractor.get_passed_assignments(course_code=parameter[1], username=parameter[0]))
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
        elif action_name == "get_today_assignments":
            return create_data_response(DatabaseExtractor.get_today_assignments(username=parameter[0]))
        elif action_name == "get_tomorrow_assignments":
            return create_data_response(DatabaseExtractor.get_tomorrow_assignments(username=parameter[0]))
        elif action_name == "get_today_events":
            return create_data_response(DatabaseExtractor.get_today_events(username=parameter[0]))
        elif action_name == "get_tomorrow_events":
            return create_data_response(DatabaseExtractor.get_tomorrow_events(username=parameter[0]))
        else:
            return create_data_response("I didn't understand anything, you probably broke me :(")

    except:
        return create_data_response("Sorry, i can not answer that.")

def create_data_response(speech: str) -> str:
    """
    Creates Json that contains the data that should be sent to API.AI
    :param speech: a string that should be put inside the json (this is the string that should be sent back to the user)
    :return: json data
    """

    data = {
        "speech": speech,
        "displayText": speech,
        "source": "pirka-chatbot-webserver"
    }
    return data


def create_followup_event_data(facebook_id: str):
    """
    This function is used when logging in with itslearning details, 
    to provide a unique login for each user 
    (link that contains the ip and port, along with the unique facebook-id) 
    :param facebook_id: facebook-id
    :return: json data
    """
    data = {
        "followupEvent": {
            "name": "custom_event",
            "data": {
                "user_id": facebook_id,
                "ip_address": ip + ":" + str(port)
            }
        }
    }

    return data


def add_ime_api_data():
    """
    This function adds all the 4000+ courses and corresponding data to the database.
    :return: Nothing
    """
    file = open("/Users/mariuskohmann/PycharmProjects/pirka/imeapi/course_codes.txt")
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
    :param username: Users username
    :param password: Users password
    :return: Nothing
    """


    # Adding a dummy-course so it is possible to test pirka with data
    DatabaseInserter.add_user_has_course(username=username, course_code="DUMMYCOURSE")
    DatabaseInserter.add_user_has_course(username=username, course_code="DUMMY2222")
    DatabaseInserter.add_user_has_course(username=username, course_code="DUMMY3333")



    # Scrapes for additional data that is user specific
    itslearning_scraper = ItsLearningScraper(username, password)
    blackboard_scraper = BlackboardScraper(username, password)

    # adds user-course relation to database
    itslearning_scraper.get_course_list()
    blackboard_scraper.get_course_list()

    # adds user's associated assignment data
    itslearning_scraper.get_all_assignments()
    blackboard_scraper.get_all_assignments()

    blackboard_scraper.close_driver()
    itslearning_scraper.close_driver()

    # add ical links
    #itslearning_scraper.get_calendar_feed()


def valid_login(username: str, password: str):
    """
    Uses scraper to test if it was entered correct username and password. Uses a global variable to keep track of valid login or not.
    :param username: username
    :param password: password
    :return: Nothing
    """

    try:
        LoginHandler.login(username, password)
        global validLogin
        validLogin = True
    except:
        validLogin = False



"""
All web endpoint functions is listed below
"""

@app.route('/', methods=['POST'])
def webhook():
    """
    Receives json data from API.AI through NGROK
    :return: The response to API.AI containing the string that should be returned to the user.
    """

    json_request = request.get_json(silent=True, force=True)


    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")

    # Then get the parameters and action_name from the result
    parameters = result.get("parameters")

    # Get the action name
    action_name = result.get("action")

    facebook_id = json_request.get("originalRequest").get("data").get("sender").get("id")

    # Retreives the username by looking up with the unique facebook id
    username = None
    try:
        username = DatabaseConnector.get_values("Select username from user where facebook_id = \"" + facebook_id + "\"")[0][0]
    except:
        username = None


    # Retrieve the course code
    course_code = parameters.get("course_code")
    parameter = [username, course_code, facebook_id]

    # Creates the string that should be sent back to the user
    print(action_name, facebook_id, course_code, parameter[0], parameter[1])
    speech = process_actions(parameter, action_name)

    # Create a response to API.AI and return it
    response = json.dumps(speech, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response


def scrape_data_from_last_user():
    """
    Scrape data after the user has successfully logged in.
    :return: The template that should be rendered when the user has sucessfully logged in.
    """

    # todo: This should be fixed, this is only getting the last user, so if a user is logging in twice, the last user will be scraped
    users = DatabaseExtractor.get_users()


    try:
        lastUsername = users[0][0]
        lastPassword = users[0][1]
    except:
        print("there was no users")


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

    error = None
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]

        thread = Thread(target=valid_login(username, password))
        thread.start()
        thread.join()

        global validLogin


        if validLogin:
            # If valid login, we add the user to the database and we render the success template
            DatabaseInserter.add_user(username, password, current_sender_id)
            validLogin = False
            scrape_data_from_last_user()
            return render_template("login_success.html")
        else:

            # If the login was not valid, we render the login screen again
            return render_template('login.html')

    return render_template('login.html')


"""
Start app
"""
if __name__ == '__main__':

    # Add all the IME-API data to the database
    #add_ime_api_data()

    # Start our webserver
    app.run(debug=True, host='', port=port, threaded=True)  # Receives action-name, gets the data and returns a string ready to send back to API.AI
