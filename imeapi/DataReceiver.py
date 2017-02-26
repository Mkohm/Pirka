import requests
import json
from datetime import datetime

base_url = "http://www.ime.ntnu.no/api/course/en/"
class DataReceiver():
    @staticmethod
    def is_valid_course(course_code: str):
        data = DataReceiver.get_data(course_code)
        try:
            cred = data["course"]["credit"]
            return True
        except TypeError:
            return False

    @staticmethod
    def get_assessment_form(course_code: str):
        # todo loop through every element in assessment

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

        return term

    @staticmethod
    def get_year(course_code: str):
        data = DataReceiver.get_data(course_code)
        year = data["course"]["assessment"][0]["realExecutionYear"]

        return year

    @staticmethod
    def is_active_course(course_code: str):

        course_year = DataReceiver.get_year(course_code)
        course_term = DataReceiver.get_term(course_code)

        # default value for end of course
        end_of_course = datetime(2000, 1, 1)

        # checks which term the course is taught, and assigns an appropiate value to end_of_course
        if course_term == "Autumn":
            end_of_course = datetime(course_year, 12, 31)
        elif course_term == "Spring":
            end_of_course = datetime(course_year, 6, 30)

        # checks if the end_of_course is in the future, and returns the boolean
        return datetime.now() < end_of_course

    @staticmethod
    def get_date_string(date: str) -> str:
        year = int(float(date[0:4]))
        month = int(float(date[5:7]))
        day = int(float(date[8:]))
        date_time = datetime(year, month, day)
        date_string = "{:%B %d, %Y}".format(date_time)
        return date_string

    @staticmethod
    def get_exam_date(course_code: str) -> str:
        # todo: make code more clean

        if not DataReceiver.is_valid_course(course_code):
            return "You entered an invalid course code."

        data = DataReceiver.get_data(course_code)

        # Get relevant data
        name = data["course"]["name"]
        try:
            exam_date = data["course"]["assessment"][0]["date"]
            exam_date_string = DataReceiver.get_date_string(exam_date)

            return "Exam date for " + str(course_code) + " " + str(name) + " is " + str(exam_date_string)
        except KeyError:
            if not DataReceiver.is_active_course(course_code):
                return "No exam date available because the course is not active"
            elif DataReceiver.get_assessment_form(course_code) != "Written examination":
                return "No exam date available because assessment form is: " + DataReceiver.get_assessment_form(
                    course_code)
            return "No exam date available"

    @staticmethod
    def get_contact_name(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            name = data["course"]["educationalRole"][0]["person"]["displayName"]
            return name
        except KeyError:
            return "No credits available"

    @staticmethod
    def get_contact_mail(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["email"]

    @staticmethod
    def get_contact_office(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["officeAddress"]

    @staticmethod
    def get_contact_phone(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["educationalRole"][0]["person"]["phone"]

    @staticmethod
    def get_contact_website(course_code) -> str:
        # gets the contacts person website

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        mail = DataReceiver.get_contact_mail(course_code)

        website_id = mail.split("@")

        return "https://www.ntnu.no/ansatte/" + website_id[0]

    @staticmethod
    def get_course_name(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["englishName"]

    @staticmethod
    def get_credit(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["credit"]

    @staticmethod
    def get_url(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        return data["course"]["infoType"][1]["text"]

    @staticmethod
    def get_prerequisite_knowledge(course_code) -> str:

        if not DataReceiver.is_valid_course(course_code):
            return "Invalid course code"

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        # Get relevant data
        return data["course"]["infoType"][2]["code"]

    @staticmethod
    def get_course_content(course_code) -> str:

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
