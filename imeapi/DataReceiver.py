import requests
import json
from datetime import datetime

base_url = "http://www.ime.ntnu.no/api/course/en/"


class DataReceiver():
    @staticmethod
    def get_exam_date(course_code: str) -> str:
        # todo: make code more clean
        # todo: fix for when written exam and still no date

        if not DataReceiver.is_valid_course(course_code):
            return "You entered an invalid course code."
        # Fetch the course
        data = DataReceiver.get_data(course_code)
        name = data["course"]["name"]

        try:
            exam_date = data["course"]["assessment"][0]["date"]
            exam_date_string = DataReceiver.format_date(exam_date)
            return "Exam date for " + str(course_code) + " " + str(name) + " is " + str(exam_date_string)
        except KeyError:
            if not DataReceiver.is_active_course(course_code):
                return "No exam date available because the course is not active."
            elif DataReceiver.get_assessment_form(course_code) != "Written examination":
                return "No exam date available because assessment form is: " + DataReceiver.get_assessment_form(
                    course_code)
            return "No exam date available"

    @staticmethod
    def get_assessment_form(course_code: str):
        # todo loop through every element in assessment

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["assessment"][0]["assessmentFormDescription"]
        except KeyError:
            return "No assesment form available"

    @staticmethod
    def get_term(course_code: str):
        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["assessment"][0]["realExecutionTerm"]
        except KeyError:
            return "Term not available"

    @staticmethod
    def get_year(course_code: str):
        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["assessment"][0]["realExecutionYear"]
        except KeyError:
            return "Year not available"

    @staticmethod
    def is_active_course(course_code: str):
        # todo check for this on a smart place.
        try:
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
        except KeyError:
            return "Can not check for active course"

    @staticmethod
    def get_contact_name(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["educationalRole"][0]["person"]["displayName"]
        except KeyError:
            return "No credits available"

    @staticmethod
    def get_contact_mail(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["educationalRole"][0]["person"]["email"]
        except KeyError:
            return "Contact mail is not available"

    @staticmethod
    def get_contact_office(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["educationalRole"][0]["person"]["officeAddress"]
        except KeyError:
            return "Office address is not available"

    @staticmethod
    def get_contact_phone(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["educationalRole"][0]["person"]["phone"]
        except KeyError:
            return "Contact phone is not available"

    @staticmethod
    def get_contact_website(course_code: str) -> str:
        # gets the contacts person website

        mail = DataReceiver.get_contact_mail(course_code)

        website_id = mail.split("@")

        return "https://www.ntnu.no/ansatte/" + website_id[0]

    @staticmethod
    def get_course_name(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["englishName"]
        except KeyError:
            return "Course name is not available"

    @staticmethod
    def get_credit(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["credit"]
        except KeyError:
            return "Course credit not available"

    @staticmethod
    def get_url(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["infoType"][1]["text"]
        except KeyError:
            return "Course url not available"

    @staticmethod
    def get_prerequisite_knowledge(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["infoType"][2]["code"]
        except KeyError:
            return "Prerequisite knowledge is not available for this course"

    @staticmethod
    def get_course_content(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["infoType"][3]["text"]
        except KeyError:
            return "Course content is not available"

    @staticmethod
    def get_course_material(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)

        try:
            return data["course"]["infoType"][4]["text"]
        except KeyError:
            return "Course material is not available"

    @staticmethod
    def get_teaching_form(course_code: str) -> str:

        # Fetch the course
        data = DataReceiver.get_data(course_code)
        try:
            return data["course"]["infoType"][5]["text"]
        except KeyError:
            return "Teaching form is not available for this course"

    @staticmethod
    def get_data(course_code: str):
        data = requests.get(base_url + course_code).json()
        return data

    @staticmethod
    def is_valid_course(course_code: str):
        data = DataReceiver.get_data(course_code)
        try:
            cred = data["course"]["credit"]
            return True
        except TypeError:
            return False

    @staticmethod
    def format_date(date: str) -> str:
        year = int(float(date[0:4]))
        month = int(float(date[5:7]))
        day = int(float(date[8:]))
        date_time = datetime(year, month, day)
        date_string = "{:%B %d, %Y}".format(date_time)
        return date_string
