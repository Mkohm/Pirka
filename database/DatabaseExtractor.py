from database import DatabaseConnector

def get_exam_date(course_code):
    date, name  = DatabaseConnector.get_values('Select exam_date, course_name from subject where '
                                               'subject.course_code = "' + course_code + '";')
    #name = DatabaseConnector.get_values("Select course_name from subject where subject.course_code = " + course_code)
    return "Exam date in " + course_code + " " + name + " is " + date
    #todo: add reason if field is empty

def get_assessment_form(course_code):
    assessment_form, name = DatabaseConnector.get_values('Select assessment_form, course_name from subject where '
                                                         'subject.course_code = "' + course_code + '";')
    return "Assessment form in " + course_code + " " + name + " is " + assessment_form

def get_contact_name(course_code):
    contact_name, name = DatabaseConnector.get_values('Select contact_name, course_name  from subject where '
                                                             'subject.course_code = "' + course_code + '";')
    return "The name of the contact person in " + course_code + " " + name + " is " + contact_name

def get_contact_mail(course_code):
    contact_mail, name = DatabaseConnector.get_values('Select contact_mail, course_name from sbject where subject.course_code = "'
                                                      + course_code + '";')
    return "The mail address of the contact person in " + course_code + " " + name + " is " + contact_mail

def get_contact_office(course_code):
    contact_office, name = DatabaseConnector.get_values('Select contact_office, course_name from subject where subject.course_code = "' +
                                                        course_code + '";')
    return "The office address of the contact person in " + course_code + " " + name + " is " + contact_office

def get_contact_phone(course_code):
    contact_phone, name = DatabaseConnector.get_values('Select contact_phone, course_name from subject where subject.course_code = "'
                                                       + course_code + '";')
    return "The phone number of the contact person in " + course_code + " " + name + " is " + contact_phone

def get_contact_website(course_code):
    contact_website, name = DatabaseConnector.get_values("Select contact_website, course_name from subject where "
                                                         'subject.course_code = "' + course_code + '";')
    return "The website of the contact person in " + course_code + " " + name + " is " + contact_website

def get_course_name(course_code):
    course_name = DatabaseConnector.get_values('Select course_name from subject where subject.course_code = "' + course_code + '";')
    return "The course name is " + course_code + " " + course_name

def get_credit(course_code):
    credit, name = DatabaseConnector.get_values('Select credit, course_name from subject where subject.course_code = "' +
                                                course_code + '" ;')
    return "The course " + course_code + " " + name + " is " + credit + " credits."

def get_url(course_code):
    url, name = DatabaseConnector.get_values('Select url, course_name from subject where subject.course_code = "' +
                                             course_code + '" ;')
    return url

def get_prereq_knowledge(course_code):
    prereq, name = DatabaseConnector.get_values('Select prereq_knowledge, course_name from subject where subject.course_code'+
                                                ' = "' + course_code + '" ;')
    return prereq

def get_course_content(course_code):
    course_content, name = DatabaseConnector.get_values('Select course_content, course_name from subject where' +
                                                        ' subject.course_code = "' + course_code + '" ;')
    return course_content

def get_course_material(course_code):
    course_material, name = DatabaseConnector.get_values('Select course_material, course_name from subject where '
                                                         'course_code = "' + course_code + '";')
    return course_material

def get_teaching_form(course_code):
    teaching_form = DatabaseConnector.get_values('Select teaching_form from subject where course_code ="' + course_code +'";')
    return teaching_form
    