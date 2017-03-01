from imeapi.DataReceiver import DataReceiver


#todo fix valid course code

class Course:
    def __init__(self, course_code: str):
        self.data = DataReceiver()
        self.assessment_form = self.data.get_assessment_form(course_code)
        self.exam_date = self.data.get_exam_date(course_code)
        self.contact_name = self.data.get_contact_name(course_code)
        self.contact_mail = self.data.get_contact_mail(course_code)
        self.contact_office = self.data.get_contact_office(course_code)
        self.contact_phone = self.data.get_contact_phone(course_code)
        self.contact_website = self.data.get_contact_website(course_code)
        self.course_name = self.data.course_name(course_code)
        self.credit = self.data.get_credit(course_code)
        self.url = self.data.get_url(course_code)
        self.prerequisite_knowledge = self.data.get_prerequisite_knowledge(course_code)
        self.course_content = self.data.get_course_content(course_code)
        self.course_material = self.data.course_material(course_code)
        self.teaching_form = self.data.get_teaching_form(course_code)










