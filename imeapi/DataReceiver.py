import requests
import json
import datetime
from datetime import datetime

base_url = "http://www.ime.ntnu.no/api/course/en/"
class DataReceiver ():

    @staticmethod
    def is_valid_course(course_code: str):
        data=DataReceiver.get_data(course_code)
        try:
            cred=data["course"]["credit"]
            return True
        except TypeError:
            return False

            
    @staticmethod
    def get_assessment_form(course_code: str):
        data = DataReceiver.get_data(course_code)
        assessment_form = data["course"]["assessment"][0]["assessmentFormDescription"]
        return assessment_form

    @staticmethod
    def get_data(course_code: str):
        data = requests.get(base_url + course_code).json()
        return data


    @staticmethod
    def get_term(course_code: str):

        data = DataReceiver.get_data(course_code)
        term = data["course"]["assessment"][0]["realExecutionTerm"]

        return term;

    @staticmethod
    def get_year(course_code: str):
        data = DataReceiver.get_data(course_code)
        year = data["course"]["assessment"][0]["realExecutionYear"]

        return year

    @staticmethod
    def is_active_course(course_code: str):
         # todo: needs better formatting
        course_year = DataReceiver.get_year(course_code)
        course_term = DataReceiver.get_term(course_code)

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        last_course_month = 1

        if (course_term == "Autumn"):
            last_course_month = 12
        elif (course_term == "Spring"):
            last_course_month = 6

        return year == course_year and month <= last_course_month

    @staticmethod
    def get_date_string(date:str)-> str:
        year = int(float(date[0:4]))
        month = int(float(date[5:7]))
        day = int(float(date[8:]))
        date_time = datetime(year, month, day)
        date_string = "{:%B %d, %Y}".format(date_time)
        return date_string

    @staticmethod
    def get_exam_date(course_code: str) -> str:
        # not the most robust code.

        data = DataReceiver.get_data(course_code)

        # Get relevant data
        name = data["course"]["name"]
        try:
            exam_date = data["course"]["assessment"][0]["date"]
            exam_date_string=DataReceiver.get_date_string(exam_date)

            return "Exam date for " + str(course_code) + " " + str(name) + " is " + str(exam_date_string)
        except KeyError:
            if (not DataReceiver.is_active_course(course_code)):
                return "No exam date available because the course is not active"
            elif (DataReceiver.get_assessment_form(course_code) != "Written examination"):
                return "No exam date available because assessment form is: " + DataReceiver.get_assessment_form(                        course_code)
            return "No exam date available"


    @staticmethod
    def get_contact_name(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            name=data["course"]["educationalRole"][0]["person"]["displayName"]
            return name
        except KeyError:
            return "No credits available"


    @staticmethod
    def get_contact_mail(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["email"]

    @staticmethod
    def get_contact_office(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["officeAddress"]

    @staticmethod
    def get_contact_phone(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["phone"]

    @staticmethod
    def get_contact_website(course_code)-> str:
        #gets the contacts person website

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        mail = DataReceiver.get_contact_mail(course_code)

        website_id = mail.split("@")

        return "https://www.ntnu.no/ansatte/" + website_id[0]

    @staticmethod
    def get_course_name(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["englishName"]

    @staticmethod
    def get_credit(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["credit"]


    @staticmethod
    def get_URL(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["infoType"][1]["text"]


    @staticmethod
    def get_prerequisite_knowledge(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        # Get relevant data
        return data["course"]["infoType"][2]["code"]

    @staticmethod
    def get_course_content(course_code)-> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["infoType"][3]["text"]


    @staticmethod
    def get_course_material(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["infoType"][4]["text"]


    @staticmethod
    def get_teaching_form(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        return data["course"]["infoType"][5]["text"]



print(DataReceiver.get_exam_date("TDT4100"))

