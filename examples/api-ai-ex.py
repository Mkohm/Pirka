# API.AI Example
# This example shows how API.AI can be used to process requests
# The connected bot will recognize requests for news, and will output the requested action and topic
# Feel free to insert your own client access token to connect your own bot
# Author: Audun Liberg

import sys, json, codecs, apiai

CLIENT_ACCESS_TOKEN = '039282428fdb49f9a226295099d3e26e'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def request():
    # Create a request
    request = ai.text_request()
    request.query = input("Say something: ")

    # Get respons, convert to json and print it
    response = request.getresponse().read().decode('utf-8')
    response = json.loads(response)
    print("Recognized action:", response["result"]["action"])
    print("Recognized topic:", response["result"]["fulfillment"]["speech"])
    print()

if __name__ == '__main__':
    while True:
        request()
