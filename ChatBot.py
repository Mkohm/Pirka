import json
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

from imeapi.Course import Course

# Flask app should start in global layout
app = Flask(__name__)
app.debug = True

# Change this variable to true if you are going to run this on Heroku
deployment = False

if deployment:
    deployment_link = "webhook"
else:
    deployment_link = ""


class ChatBot:
    # Starts the webserver and is ready to listen to incoming actions
    def __init__(self):
        # Change this variable to true if you are going to run this on Heroku
        self.deployment = False

        # The port to run webserver on
        self.port = int(os.getenv('PORT', 8080))

        # Run application
        app.run(debug=True, port=self.port, host='localhost')
        print("Starting chatbot-app on port %d" % self.port)

    # Receives action-name, gets the data and returns a string ready to send back to API.AI
    @staticmethod
    def process_actions(parameter: str, action_name: str) -> str:
        if action_name == "get_exam_date":
            return Course.get_exam_date(parameter)


@app.route('/', methods=['POST', 'GET'])
def login():
    """
    This method handles the login so we can get user information to the blackboard scraper.
    We load a template so the user can login and send us the email and password.
    :return:
    """

    error = None
    if request.method == 'POST':

        #If the login is successfull we return a template saying you can start using pirka
        if valid_login(request.form['email'], request.form['password']):
            return render_template("login_success.html")

        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username:str, password:str):
    #Try to do blackboard scraping
    print(username)
    print(password)




    return True


@app.route('/' + deployment_link, methods=['POST'])
def webhook():
    json_request = request.get_json(silent=True, force=True)

    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")

    # Then get the parameters of the result
    parameters = result.get("parameters")
    parameter = parameters.get("course_code")

    action_name = result.get("action")

    speech = ChatBot.process_actions(parameter, action_name)

    data = {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

    response = json.dumps(data, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response


# Start the application
bot = ChatBot()
