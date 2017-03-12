# Pirka - the student helper
A chatbot developed using API.AI and a python web server. Release date of Pirka is 27.april 2017

![Pirka running](https://github.com/Mkohm/Pirka/blob/dev/demo_pictures/pirka.png "Pirka running")

## Usage
The first time you want to use Pirka you have to visit: https://www.facebook.com/pirkabot/ and then click to send a message to Pirka.

## Features

- [x] Can ask when an exam in a course is
- [ ] Can get a list of exersizes to do

## Setup for contributing to Pirka

### Requirements
- Python 3.6 (or some other Python 3 version)
- Ngrok (download here: https://ngrok.com/)
- API.AI account and an agent (go to https://api.ai/ to create one)

### Installation
1. cd into your folder where you downloaded ngrok, then do:
```
./ngrok http 8080
```
The result will be something like this:

![Ngrok forwards requests to localhost](https://github.com/Mkohm/Pirka/blob/master/ngrok.png "Ngrok forwards requests to localhost")

Ngrok will now forward all connections to localhost.

2. Copy the address that is hightligted in the picture above.
3. Log in to API.AI and go to fulfillment and enable webhook. Paste the address so API.AI can send POST requests to Ngrok.
4. Clone this project into a new folder
5. Get all the required python libraries: Cd into the project folder and do:
```
pip install requirements.txt
```
6. You can now run ChatBot.py to start the webserver and start developing
