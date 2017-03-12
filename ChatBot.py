import json
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from scraper.BlackboardScraper import BlackboardScraper

from imeapi.Course import Course

# Flask app should start in global layout
app = Flask(__name__)
app.debug = True

# Change this variable to true if you are going to run this on Heroku
deployment = True
pirka_users = {}

if deployment:
    deployment_link = "webhook"
else:
    deployment_link = ""


class ChatBot:
    # Starts the webserver and is ready to listen to incoming actions
    def __init__(self):
        # Change this variable to true if you are going to run this on Heroku
        self.deployment = deployment


        # Bind to PORT if defined, otherwise default to 5000.
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)


    # Receives action-name, gets the data and returns a string ready to send back to API.AI
    @staticmethod
    def process_actions(parameter: str, action_name: str) -> str:
        if action_name == "login":
            return ChatBot.create_followup_event_data(parameter)
        elif action_name == "get_exam_date":
            return ChatBot.create_data_response(Course(parameter).get_exam_date())
        elif action_name == "get_assessment_form":
            return ChatBot.create_data_response(Course(parameter).get_assessment_form())
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

    error = None
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]

        #If the login is successfull we return a template saying you can start using pirka
        if valid_login(username, password):

            pirka_users[current_sender_id] = {username, password}
            return render_template("login_success.html")
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username:str, password:str):
    #Try to do blackboard scraping

    try:
        scraper = BlackboardScraper(username, password)
        return True
    except:
        return False


@app.route('/' + deployment_link, methods=['POST'])
def webhook():
    print(pirka_users)
    json_request = request.get_json(silent=True, force=True)

    print(json.dumps(json_request, indent=4))

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
    elif action_name == "get_exam_date":
        parameter = parameters.get("course_code")


    speech = ChatBot.process_actions(parameter, action_name)


    print(json.dumps(speech, indent=4))
    response = json.dumps(speech, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response

# Start the application
bot = ChatBot()
