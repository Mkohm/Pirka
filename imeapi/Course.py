import requests
from datetime import datetime
from DataReceiver import DataReceiver

class Course:
    def __init__(self, course_code: str):
        self.data = DataReceiver()
        self.assessment_form = self.get_assessment_form()
        self.data = self.exam_data.get_data(course_code)
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


    def get_data(self, course_code: str):
        if self.is_valid_course():
            base_url = "http://www.ime.ntnu.no/api/course/en/"
            data = requests.get(base_url + course_code).json()
            return data


    def get_assessment_form(self, course_code: str):
        if self.field_exist():

            # todo loop through every element in assessment
            assessment_form = self.data["course"]["assessment"][0]["assessmentFormDescription"]
            return assessment_form

DataReceiver.get_exam_date()






@staticmethod
    def format_date(date: str) -> str:
        year = int(float(date[0:4]))
        month = int(float(date[5:7]))
        day = int(float(date[8:]))
        date_time = datetime(year, month, day)
        date_string = "{:%B %d, %Y}".format(date_time)
        return date_string

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



    def __field_exist__(field, self):
        try:
            if field == "exam_date":
                date = self.data["course"]["assessment"][0]["date"]
                return True
            elif field == "assessment_form":
                assessment_form = self.data["course"]["assessment"][0]["assessmentFormDescription"]
                return True
            elif field == "contact_name":
                name = self.data["course"]["educationalRole"][0]["person"]["displayName"]
                return True
            elif field == "contact_office":
                office = self.data["course"]["educationalRole"][0]["person"]["officeAddress"]
                return True
            elif field == "contact_phone":
                phone = self.data["course"]["educationalRole"][0]["person"]["phone"]
                return True
            elif field == "course_name":
                name = self.data["course"]["englishName"]
                return True
            elif field == "credit":
                credit = self.data["course"]["credit"]
                return True
            elif field == "url":
                url = self.data["course"]["infoType"][1]["text"]
                return True
            elif field == "prerequisite_knowledge":
                knowledge = self.data["course"]["infoType"][2]["code"]
                return True
            elif field == "course_content":
                content = self.data["course"]["infoType"][3]["text"]
                return True
            elif field == "course_material":
                material = self.data["course"]["infoType"][4]["text"]
                return True
            elif field == "teaching_form":
                form = self.data["course"]["infoType"][5]["text"]
                return True
            else:
                return False

        except KeyError:
            return False


    def is_valid_course(self):
        return self.field_exist("credit")







