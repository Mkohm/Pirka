# **WARNING**
This software is in development and stores your username and password unsecurely. Run the software locally on your computer to avoid security risks. 

# Pirka - the student helper
A chatbot developed using API.AI and a python web server. Release date of Pirka is 27.april 2017

![Pirka](https://scontent-arn2-1.xx.fbcdn.net/v/t31.0-8/18077390_722541831261768_7727061630711910667_o.jpg?oh=09daf4894e8e18e1036c598a1d92e92d&oe=59859C1A "Pirka")

## Usage
The first time you want to use Pirka you have to visit: https://www.facebook.com/pirkabot/ and then click to send a message to Pirka. You will then have to login with your Itslearning/Blackboard login details to get all the functionality. When you have entered your details Pirka will scrape data from Itslearing & Blackboard, this will take some time (around -5 minutes), please be patient.

### Example usages
#### Using context
- User: "Can i get the exam date in TDT4100?"
- Pirka: "The exam date in TDT4100 is..."
- User: "Name of the contact person?"
- Pirka: "The name of the contact person in **TDT4100** is Hallvard Trætteberg" (Pirka remembers the course code you talked about in the last messages)




#### Course specific usage
- What is the exam date?
- What is the exam date in TDT4100
- How am I assessed? 
- What is the contact mail?
- What is the name of the contact person?
- What is the phone number to the contact person?
- What is the contact website?
- What office does the contact person have?
- What is the teaching form?
- What is the course name?
- How many credits is there for TDT4100?
- Send me the link to the course home page. 
- What’s the pre required knowledge?
- Get course content
- Which book do I need?
- Get teaching form

#### User specific usage
- What is the exercise status?
- Have I passed the assignment scheme?
- How many exercises do i have left?
- What is the project status?
- What is the lab status?
- When is my next due date? 
- What’s my next event? 
- Where and when is my next lecture? 
- Can you give me this weeks schedule?
- Can you give me next weeks assignments?
- Can you give me next weeks events?
- Can you give me this weeks assignments?
- Can you give me this weeks events?
- Do I have any assignments due today?
- Do i have any assignments tomorrow?
- Do i have any events today?
- Do i have any events tomorrow?
- Can you give me all passed assignments?
- What are my exam dates?
- How many days are there until my first exam?
- Should i start to read for my exam?
- Can i get a list of my course codes?
- Which courses am I participating in? 
- How many courses do i have?

## Planned Future features 
- [ ] Get links to the assignments
- [ ] Push notifications for assignments that soon needs to be delivered
- [ ] Push notifications for upcoming events

# Want to contribute? **Setup for contributing to Pirka**

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
