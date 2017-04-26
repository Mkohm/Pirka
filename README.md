- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`


# Pirka - the student helper
A chatbot developed using API.AI and a python web server. Release date of Pirka is 27.april 2017

![Pirka running](https://github.com/Mkohm/Pirka/blob/dev/demo_pictures/pirka.png "Pirka running")

## Usage
The first time you want to use Pirka you have to visit: https://www.facebook.com/pirkabot/ and then click to send a message to Pirka.

### Example usages
- stoehu
- staho
- shoe

## Non personal features

- [x] Can ask when an exam in a course is
- [x] Can login to get personal Itslearning and Blackboard data
- [x] Can get the name, phonenumber, office, email to the contact person in a course
- [x] Can get a courses website, teaching form, credit, url, prerequisite knowledge, course content, course material, assessment form

## Personal features
- [x] Can get exercise status
- [x] Can get next event
- [x] Can get next assignment
- [x] Can get this weeks schedule (assignments + events)
- [x] Can get next weeks schedule (assignments + events)
- [x] Can get this weeks events
- [x] Can get this weeks assignments
- [x] Can get next weeks events
- [x] Can get next weeks assignments
- [x] Can get number of days until your first exam
- [x] Can get a list of all your exam dates
- [x] Can get a list of all your course codes
- [x] Can get a list of all your course names
- [x] Can get the number of courses your are participating in

## Future 
- [ ] Get links to the assignments
- [ ] Push notifications for 



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

![Ngrok forwards requests to localhost](https://raw.githubusercontent.com/Mkohm/Pirka/master/demo_pictures/ngrok.png "Ngrok forwards requests to localhost")


# ![Ngrok forwards requests to localhost](https://raw.githubusercontent.com/Mkohm/Pirka/dev/demo_pictures/ngrok.png "Ngrok forwards requests to localhost")



Ngrok will now forward all connections to localhost.

2. Copy the address that is hightligted in the picture above.
3. Log in to API.AI and go to fulfillment and enable webhook. Paste the address so API.AI can send POST requests to Ngrok.
4. Clone this project into a new folder
5. Get all the required python libraries: Cd into the project folder and do:
```
pip install requirements.txt
```
You can now run ChatBot.py to start the webserver and start developing
