import requests
import json

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
    def get_data(course_code: str):
        data = requests.get(base_url + course_code).json()
        return data

    @staticmethod
    def get_exam_date(course_code: str) -> str:
        if not DataReceiver.is_valid_course(course_code):
            return "You entered an invalid course code."


        data = DataReceiver.get_data(course_code)

        # Get relevant data
        name = data["course"]["name"]
        try:
            exam_date = data["course"]["assessment"][0]["date"]
            return "The exam date for " + str(course_code) + " " + str(name) + " is " + str(exam_date) + "."
        except KeyError:
            #todo: add reason, e.g. wrong semester, different evaluation form
            return "There is no exam date available."

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



