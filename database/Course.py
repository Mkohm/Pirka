import requests
from datetime import datetime

base_url = "http://www.ime.ntnu.no/api/course/en/"


class Course:
    def __init__(self, course_code: str):
        self.course_code = course_code

        self.events = []
        self.exam_date = None
        self.assessment_form = None
        self.term = None
        self.year = None
        self.course_active = None
        self.contact_name = None
        self.contact_office = None
        self.contact_phone = None
        self.contact_website = None
        self.course_name = None
        self.credit = None
        self.url = None
        self.prereq_knowledge = None
        self.course_content = None
        self.course_material = None
        self.teaching_form = None

        self.events = []

    def set_exam_date(self):

        # todo: make code more clean
        # todo: fix for when written exam and still no date
        # todo: move check for valid course?
        # todo: fix the active course checker

        if not self.is_valid_course():
            self.exam_date = "You entered an invalid course code."
            return

        # Fetch the course
        data = self.get_data()
        name = self.get_course_name()

        try:
            exam_date = data["course"]["assessment"][0]["date"]
            exam_date_string = self.format_date(exam_date)
            self.exam_date = "Exam date for " + str(self.course_code) + " " + str(name) + " is " + str(exam_date_string)
        except KeyError:
            self.set_is_active_course()
            self.get_assessment_form()

            if not self.course_active:
                self.exam_date = "No exam date available because the course is not active."
            elif self.assessment_form != "Written examination":
                self.exam_date = "No exam date available because assessment form is: " + self.assessment_form
            else:
                self.exam_date = "No exam date available"

    def get_exam_date(self) -> str:
        self.set_exam_date()
        return self.exam_date

    def set_assessment_form(self):
        # todo loop through every element in assessment

        # Fetch the course
        data = self.get_data()
        number = len(data["course"]["assessment"])
        liste = [0] * number
        for i in range(0, number):
            try:
                liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
            except KeyError:
                self.assessment_form = "No assessment form available"

        self.assessment_form = ' and '.join(liste)

    def get_assessment_form(self):
        self.set_assessment_form()
        return self.assessment_form

    def set_term(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.term = data["course"]["assessment"][0]["realExecutionTerm"]
        except KeyError:
            self.term = "Term not available"

    def get_term(self):
        self.set_term()
        return self.term

    def set_year(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.year = int(data["course"]["assessment"][0]["realExecutionYear"])
        except KeyError:
            self.year = "Year not available"

    def get_year(self):
        self.set_year()
        return self.year

    def set_is_active_course(self):
        # todo check for this on a smart place.
        try:
            self.get_year()
            self.get_term()

            # default value for end of course
            end_of_course = None

            # checks which term the course is taught, and assigns an appropiate value to end_of_course
            if self.term == "Autumn":
                end_of_course = datetime(self.year, 12, 31)
            elif self.term == "Spring":
                end_of_course = datetime(self.year, 6, 30)

            # checks if the end_of_course is in the future, and returns the boolean
            self.course_active = datetime.now() < end_of_course

        except KeyError:
            self.course_active = "Can not check for active course"

    def get_is_active_course(self):
        self.set_is_active_course()
        return self.course_active
    #todo: add in DatabaseExtractor

    def set_contact_name(self):
        # Fetch the course
        data = self.get_data()

        try:
            self.contact_name = data["course"]["educationalRole"][0]["person"]["displayName"]
        except KeyError:
            self.contact_name = "No contact person available"

    def get_contact_name(self) -> str:
        self.set_contact_name()
        return self.contact_name

    def set_contact_mail(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.contact_mail = data["course"]["educationalRole"][0]["person"]["email"]
        except KeyError:
            self.contact_mail = "Contact mail is not available"

    def get_contact_mail(self) -> str:
        self.set_contact_mail()
        return self.contact_mail

    def set_contact_office(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.contact_office = data["course"]["educationalRole"][0]["person"]["officeAddress"]
        except KeyError:
            self.contact_office = "Office address is not available"

    def get_contact_office(self) -> str:
        self.set_contact_office()
        return self.contact_office

    def set_contact_phone(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.contact_phone = data["course"]["educationalRole"][0]["person"]["phone"]
        except KeyError:
            self.contact_phone = "Contact phone is not available"

    def get_contact_phone(self) -> str:
        self.set_contact_phone()
        return self.contact_phone

    def set_contact_website(self):
        # gets the contacts person website
        mail = self.get_contact_mail()
        website_id = mail.split("@")

        self.contact_website = "https://www.ntnu.no/ansatte/" + website_id[0]

    def get_contact_website(self) -> str:
        self.set_contact_website()
        return self.contact_website

    def set_course_name(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.course_name = data["course"]["englishName"]
        except KeyError:
            self.course_name = "Course name is not available"

    def get_course_name(self) -> str:
        self.set_course_name()
        return self.course_name

    def set_credit(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.credit = data["course"]["credit"]
        except KeyError:
            self.credit = "Course credit not available"

    def get_credit(self):
        self.set_credit()
        return self.credit

    def set_url(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.url = data["course"]["infoType"][1]["text"]
        except KeyError:
            self.url = "Course url not available"

    def get_url(self) -> str:
        self.set_url()
        return self.url

    def set_prereq_knowledge(self):
        # Fetch the course
        data = self.get_data()
        value = ""

        for i in range(0, 6):
            try:
                value = data["course"]["infoType"][i]["code"]
                if (value == "ANBFORK"):
                    index = i
            except KeyError:
                self.prereq_knowledge = "Prerequisite knowledge is not available for this course"
        try:
            self.prereq_knowledge = data["course"]["infoType"][index]["text"]
        except KeyError:
            self.prereq_knowledge = "Prerequisite knowledge is not available for this course"

    def get_prereq_knowledge(self) -> str:
        self.set_prereq_knowledge()
        return self.prereq_knowledge

    def set_course_content(self):
        # Fetch the course
        data = self.get_data()
        x = len(data["course"]["infoType"])
        index = 0
        for i in range(0, x):
            try:
                name = data["course"]["infoType"][i]["name"]
                if (name == "Academic content"):
                    index = i
            except KeyError:
                self.course_content = "Course content is not available"
        try:
            self.course_content = data["course"]["infoType"][index]["text"]
        except KeyError:
            self.course_content = "Course content is not available"

    def get_course_content(self) -> str:
        self.set_course_content()
        return self.course_content

    def set_course_material(self):
        # Fetch the course
        data = self.get_data()
        x = len(data["course"]["infoType"])
        index = 0
        for i in range(0, x):
            try:
                name = data["course"]["infoType"][i]["name"]
                if (name == "Course materiel"):
                    index = i
            except KeyError:
                self.course_content = "Course material is not available"
        try:
            self.course_material = data["course"]["infoType"][index]["text"]
        except KeyError:
            self.course_material = "Course material is not available"

    def get_course_material(self) -> str:
        self.set_course_material()
        return self.course_material

    def set_teaching_form(self):
        # Fetch the course
        data = self.get_data()
        try:
            self.teaching_form = data["course"]["infoType"][5]["text"]
        except KeyError:
            self.teaching_form = "Teaching form is not available for this course"

    def get_teaching_form(self) -> str:
        self.set_teaching_form()
        return self.teaching_form

    def set_events(self):
        pass

    def get_events(self):
        self.set_events()
        return self.events

    def get_data(self):
        data = requests.get(base_url + self.course_code).json()
        return data

    def is_valid_course(self):
        data = self.get_data()
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


