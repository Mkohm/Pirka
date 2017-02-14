#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

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


    response = processRequest(jsonRequest)
    response = json.dumps(response, indent=4)
    print(response)

    r = make_response(response)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "yahooWeatherForecast":
        return {}
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {}
    api_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result = urllib.request.urlopen(api_url).read()
    data = json.loads(result)
    result = makeWebhookResult(data)

    print("Result: " + result)

    return result



def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

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

    print("halla " + json.dumps(item, indent=4))

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
    app.run(debug=False, port=port, host='localhost')