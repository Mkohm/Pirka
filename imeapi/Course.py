import requests
from datetime import datetime

class Course:
    def __init__(self, course_code: str):
        self.assessment_form = self.get_assessment_form()
        self.data = self.get_data(course_code)
        self.exam_date = self.get_exam_date()
        self.contact_name = self.get_contact_name()
        self.contact_mail = self.get_contact_mail()
        self.contact_office = self.get_contact_office()
        self.contact_phone = self.get_contact_phone()
        self.contact_website = self.get_contact_website()
        self.course_name = self.course_name()
        self.credit = self.get_credit()
        self.url = self.get_url()
        self.prerequisite_knowledge = self.get_prerequisite_knowledge()
        self.course_content = self.get_course_content()
        self.course_material = self.course_material()
        self.teaching_form = self.get_teaching_form()

    def get_data(course_code: str):
        base_url = "http://www.ime.ntnu.no/api/course/en/"
        data = requests.get(base_url + course_code).json()
        return data

    def get_term(self):
        term = self.data["course"]["assessment"][0]["realExecutionTerm"]
        return term


    def get_year(self):
        year = self.data["course"]["assessment"][0]["realExecutionYear"]
        return year


    def __is_active_course__(self):
        course_year = self.get_year()
        course_term = self.get_term()

        # default value for end of course
        end_of_course = datetime(2000, 1, 1)

        # checks which term the course is taught, and assigns an appropiate value to end_of_course
        if course_term == "Autumn":
            end_of_course = datetime(course_year, 12, 31)
        elif course_term == "Spring":
            end_of_course = datetime(course_year, 6, 30)

        # checks if the end_of_course is in the future, and returns the boolean
        return datetime.now() < end_of_course

    def __field_exist__(field):
        try:
            if field == "exam_date":
            elif field == ""
            return exist
        except KeyError:
            return "Empty field"



    def make_course_dict(self):


        course_address = {key, value}


