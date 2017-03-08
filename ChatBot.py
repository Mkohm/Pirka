import json
import os
from flask import Flask
from flask import request
import requests
from flask import make_response
from flask import render_template
from scraper.BlackboardScraper import BlackboardScraper

from imeapi.Course import Course

# Flask app should start in global layout
app = Flask(__name__)
app.debug = True



facebook_id = {}
current_sender_id = None

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
            return Course(parameter).get_exam_date()
        elif action_name == "login":
            #save user data
            pass
        else:
            return "I didnt understand shit, you probably broke me :("





@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    This method handles the login so we can get user information to the blackboard scraper.
    We load a template so the user can login and send us the email and password.
    :return:
    """

    error = None
    if request.method == 'POST':

        #If the login is successfull we return a template saying you can start using pirka
        if valid_login(request.form['username'], request.form['password']):

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
        facebook_id[current_sender_id] = {username, password}


        print()
        print(facebook_id)
        return True
    except:
        return False


@app.route('/' + deployment_link, methods=['POST'])
def webhook():
    json_request = request.get_json(silent=True, force=True)

    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")



    # Then get the parameters of the result
    parameters = result.get("parameters")
    parameter = parameters.get("course_code")

    action_name = result.get("action")

    if action_name == "login":
        print(json_request)
        facebook_sender_id = result.get("contexts")[0].get("parameters").get("facebook_sender_id")
        current_sender_id = facebook_sender_id


    data = None
    if action_name == "loginlogin":
        print("loginlogin")
        facebook_sender_id = result.get("contexts")[0].get("parameters").get("facebook_sender_id")
        print(facebook_sender_id)

        data = {
                                                "id": "0cdb5479-fb34-489f-8631-d733308a1b3f",
                                      "timestamp": "2017-03-08T18:15:54.828Z",
                                      "lang": "en",
                                      "result": {
                                        "source": "agent",
                                        "resolvedQuery": "login",
                                        "action": "login",
                                        "actionIncomplete": "false",
                                        "parameters": {},
                                        "contexts": [],
                                        "metadata": {
                                          "intentId": "580b1de5-9a96-439b-a450-f7ce6ad9b2e5",
                                          "webhookUsed": "true",
                                          "webhookForSlotFillingUsed": "false",
                                          "intentName": "login"
                                        },
                                        "fulfillment": {
                                          "speech": "",
                                          "messages": [
                                            {
                                              "type": "0",
                                              "speech": ""
                                            },
                                            {
                                              "title": "Itslearning integration",
                                              "subtitle": "login",
                                              "imageUrl": "https://raw.githubusercontent.com/Mkohm/Pirka/dev/login.png",
                                              "buttons": [
                                                {
                                                  "text": "Click here to enable itslearning integration",
                                                  "postback": "http://localhost:8080/login/detteersmud"
                                                }
                                              ],
                                              "type": "1"
                                            }
                                          ]
                                        },
                                        "score": "1"
                                      },
                                      "status": {
                                        "code": "206",
                                        "errorType": "partial_content",
                                        "errorDetails": "Webhook call failed. Error message: org.springframework.web.client.HttpServerErrorException: 500 INTERNAL SERVER ERROR ErrorId: 17aeb4ac-5cb2-4139-8351-a7854935c094"
                                      },
                                      "sessionId": "2edb215c-493a-49d8-b317-6375ef759897"
        }

        """

                    speech = ChatBot.process_actions(parameter, action_name)

                        data = {
                                "speech": speech,
                                "displayText": speech,
                                # "data": data,
                                # "contextOut": [],
                                "source": "Pirka-chatbot-webserver"
                        }
        """



    print(json.dumps(data, indent=4))
    response = json.dumps(data, indent=4)
    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response

# Start the application
bot = ChatBot()
