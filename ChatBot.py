import urllib3.request, urllib.parse, urllib.error
import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout
app = Flask(__name__)
app.debug = True

# Change this variable to true if you are going to run this on Heroku
deployment = False

if deployment:
    deployment_link = "webhook"
else:
    deployment_link = ""


class ChatBot():


    #Starts the webserver and is ready to listen to incoming actions
    def __init__(self):

        # Change this variable to true if you are going to run this on Heroku
        self.deployment = False


        # The port to run webserver on
        self.port = int(os.getenv('PORT', 8080))


        # Run application
        app.run(debug=True, port=self.port, host='localhost')
        print("Starting chatbot-app on port %d" % self.port)


    # Receives action-name, gets the data and returns a string ready to send back to API.AI
    def processActions(self, actionName: str) -> str:
        return "Dette er en test"



    def sendToAPIAI(self, messageToUser: str, actionName: str):
        response = self.processActions(actionName)
        response = json.dumps(response, indent=4)
        print(response)

        created_response = make_response(response)
        created_response.headers['Content-Type'] = 'application/json'

        return created_response

@app.route('/' + deployment_link, methods=['POST'])
def webhook():
    print("webhook kallt")





# Start the application
bot = ChatBot()



