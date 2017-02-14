#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
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



@app.route('/' + deployment_link, methods=['POST'])
def webhook():

    # This is the json-data we are sent from API.AI (request in json-form)
    jsonRequest = request.get_json(silent=True, force=True)

    # This is just printing the jsonRequest with all the data
    print("Request:")
    print(json.dumps(jsonRequest, indent=4))

    # This is creating a response to the request
    response = processRequest(jsonRequest)
    response = json.dumps(response, indent=4)
    print(response)

    created_response = make_response(response)
    created_response.headers['Content-Type'] = 'application/json'

    return created_response


def processRequest(json_request):

    # Here we can add different cases depending on the names on the different actions
    if json_request.get("result").get("action") != "yahooWeatherForecast":
        return {}

    yahoo_query = makeYahooQuery(json_request)

    if yahoo_query is None:
        #return {}
        return {}


    base_url = "https://query.yahooapis.com/v1/public/yql?"
    # This variable contains a link to the json data we got from Yahoo
    received_link_to_json = base_url + urllib.parse.urlencode({'q': yahoo_query}) + "&format=json"

    # This is the json data we get from yahoo containing our weather information
    result = requests.get(received_link_to_json, verify=False).text
    print(result)


    data = json.loads(result)
    result = makeWebhookResult(data)

    return result



def makeYahooQuery(json_request):

    # Extract the data from the json-request (first get the result section of the json)
    result = json_request.get("result")

    # Then get the parameters of the result
    parameters = result.get("parameters")

    # Extract the city from the result
    city = parameters.get("geo-city")

    if city is None:
        return None

    # If we got the parameters in the json_request - create this query to get the data from yahoo
    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"

def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    print(json.dumps(item, indent=4))

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)


    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


# This starts the program
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))

    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='localhost')