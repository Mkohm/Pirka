from database import DatabaseConnector

@staticmethod
def get_exam_date(course_code):
    date, name  = DatabaseConnector.get_values("Select exam_date, course_name from subject where "
                                               "subject.course_code = " + course_code)
    #name = DatabaseConnector.get_values("Select course_name from subject where subject.course_code = " + course_code)
    return "Exam date in " + course_code + " " + name + " is " + date
    #todo: add reason if field is empty

@staticmethod
def get_assessment_form(course_code):
    assessment_form, name = DatabaseConnector.get_values("Select assessment_form, course_name from subject where "
                                                         "subject.course_code = " + course_code)
    return "Assessment form in " + course_code + " " + name + " is " + assessment_form

@staticmethod
def get_contact_name(course_code):
    contact_name, name = DatabaseConnector.get_values("Select contact_name, course_code  from subject where "
                                                             "subject.course_code = " + course_code)
    return "The name of the contact person in " + course_code + " " + name + " is " + contact_name

@staticmethod
def get_contact_mail(course_code):
    contact_mail, name = DatabaseConnector.get_values("Select contact_mail from sbject where subject.course_code = "
                                                      + course_code)
    return "The mail address of the contact person in " + course_code + " " + name + " is " + contact_mail


@staticmethod
def get_contact_office(course_code):
    contact_office, name = DatabaseConnector.get_values("Select contact_office from subject where course.code = " +
                                                        course_code)
    return "The office address of the contact person in " + course_code + " " + name + " is " + contact_office

@staticmethod
def get_



