import json
import os

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

from database import DatabaseConnector
from database import DatabaseInserter
from database.Course import Course
from scraper.ItsLearningScraper import ItsLearningScraper

# Flask app should start in global layout
app = Flask(__name__)
app.debug = True

# Change this variable to true if you are going to run this on Heroku
deployment = False
pirka_users = {}

if deployment:
    deployment_link = "webhook"
else:
    deployment_link = ""



class ChatBot:
    # Starts the webserver and is ready to listen to incoming actions
    def __init__(self):
        # Change this variable to true if you are going to run this on Heroku
        self.deployment = False


        # todo: Create thread to set all data in the database, start scraping



        # The port to run webserver on
        self.port = int(os.getenv('PORT', 8080))

        # Run application
        app.run(debug=True, port=self.port, host='localhost')
        print("Starting chatbot-app on port %d" % self.port)

    # Receives action-name, gets the data and returns a string ready to send back to API.AI
    @staticmethod
    def process_actions(parameter: str, action_name: str) -> str:
        if action_name == "login":
            return ChatBot.create_followup_event_data(parameter)
        elif action_name == "get_exam_date":
            return ChatBot.create_data_response(Course(parameter).get_exam_date())
        elif action_name == "get_assessment_form":
            return ChatBot.create_data_response(Course(parameter).get_assessment_form())
        elif action_name == "get_contact_mail":
            return ChatBot.create_data_response(Course(parameter).get_contact_mail())
        elif action_name == "get_contact_name":
            return ChatBot.create_data_response(Course(parameter).get_contact_name())
        elif action_name =="get_contact_phone":
            return ChatBot.create_data_response(Course(parameter).get_contact_phone())
        elif action_name =="get_contact_website":
            return ChatBot.create_data_response(Course(parameter).get_contact_website())
        elif action_name== "get_office":
            return ChatBot.create_data_response(Course(parameter).get_office())
        elif action_name == "get_teaching_form":
            return ChatBot.create_data_response(Course(parameter).get_teaching_form())
        elif action_name == "get_course_name":
            return ChatBot.create_data_response(Course(parameter).get_course_name())
        elif action_name == "get_credit":
            return ChatBot.create_data_response(Course(parameter).get_credit())
        elif action_name == "get_url":
            return ChatBot.create_data_response(Course(parameter).get_url())
        elif action_name == "get_prereq_knowledge":
            return ChatBot.create_data_response(Course(parameter)).get_prereq_knowledge()
        elif action_name =="get_course_content":
            return ChatBot.create_data_response(Course(parameter).get_course_content())
        elif action_name == "get_course_material":
            return ChatBot.create_data_response(Course(parameter).get_course_material())
        elif action_name == "get_teaching_form":
            return ChatBot.create_data_response(Course(parameter).get_teaching_form())
        else:
            return "I didn't understand shit, you probably broke me :("

    @staticmethod
    def create_data_response(speech: str) -> str:
        data = {
            "speech": speech,
            "displayText": speech,
            # "data": data,
            # "contextOut": [],
            "source": "Pirka-chatbot-webserver"
        }
        return data

    @staticmethod
    def create_followup_event_data(parameter_value: str):
        data = {
            "followupEvent": {
                "name": "custom_event",
                "data": {
                    "user_id": parameter_value
                }
            }
        }

        return data


@app.route('/login/<current_sender_id>', methods=['POST', 'GET'])
def login(current_sender_id):
    """
    This method handles the login so we can get user information to the blackboard scraper.
    We load a template so the user can login and send us the email and password.
    :return:
    """

    print("login test")

    error = None
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]

        # If the login is successfull we return a template saying you can start using pirka
        if valid_login(username, password):

            #pirka_users[current_sender_id] = {username, password}

            DatabaseInserter.add_user(username, password, current_sender_id)

            return render_template("login_success.html")
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def valid_login(username: str, password: str):
    # Try to do blackboard scraping

    print(username)
    print(password)
    try:
        scraper = ItsLearningScraper(username, password)

        print("Login success")
        return True
    except:
        print("Login failed")
        return False


@app.route('/' + deployment_link, methods=['POST'])
def webhook():
    json_request = request.get_json(silent=True, force=True)

    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")

    # Then get the parameters and action_name of the result
    parameters = result.get("parameters")

    action_name = result.get("action")

    #Handles different parameters to the process-actions method
    if action_name == "login":

        #Depending on if the event "WELCOME_FACEBOOK" or if the user typed "login, get started ect" the
        # resulting json request is different, hence we get the parameter in different ways
        if len(result.get("contexts")) > 1:
            parameter = result.get("contexts")[1].get("parameters").get("facebook_sender_id")
        else:
            parameter = result.get("contexts")[0].get("parameters").get("facebook_sender_id")
    else:
        parameter = parameters.get("course_code")


    speech = ChatBot.process_actions(parameter, action_name)


    response = json.dumps(speech, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response


# Start the application
bot = ChatBot()