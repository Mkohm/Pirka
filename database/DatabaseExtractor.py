from database import DatabaseConnector
#todo: make possible for nontype fields

def get_exam_date(course_code):
    print("Getting exam date ...")
    print(course_code)
    ans = DatabaseConnector.get_values("Select exam_date, course_name from course where "
                                               "course.course_code = \"" + course_code + "\";")

    date = ans[0][0]
    name=ans[0][1]
    return "Exam date in " + course_code + " " + name + " is " + date
    #todo: add reason if field is empty

def get_assessment_form(course_code):
    ans = DatabaseConnector.get_values('Select assessment_form, course_name from course where '
                                                         'course.course_code = "' + course_code + '";')
    assessment_form=ans[0][0]
    name=ans[0][1]
    return "Assessment form in " + course_code + " " + name + " is " + assessment_form

def get_contact_name(course_code):
    ans = DatabaseConnector.get_values("Select contact_name, course_name  from course where "
                                                             "course.course_code = \"" + course_code + "\";")
    contact_name=ans[0][0]
    name=ans[0][1]
    return "The name of the contact person in " + course_code + " " + name + " is " + contact_name

def get_contact_mail(course_code):
    ans = DatabaseConnector.get_values("Select contact_mail, course_name from course where course.course_code = \""
                                                      + course_code + "\";")
    contact_mail=ans[0][0]
    name=ans[0][1]
    return "The mail address of the contact person in " + course_code + " " + name + " is " + contact_mail

def get_contact_office(course_code):
    ans = DatabaseConnector.get_values("Select contact_office, course_name from course where course.course_code = \""
                                       + course_code + "\";")
    contact_office=ans[0][0]
    name=ans[0][1]

    if contact_office == "null":
        return "There is no existing office address in " + course_code + " " + name
    else:
        return "The office address of the contact person in " + course_code + " " + name + " is " + contact_office

def get_contact_phone(course_code):
    ans = DatabaseConnector.get_values("Select contact_phone, course_name from course where course.course_code = \""
                                                       + course_code + "\";")
    contact_phone=ans[0][0]
    name=ans[0][1]

    if contact_phone == "null":
        return "There is no phone number available in " + course_code + " " + name
    else:
        return "The phone number of the contact person in " + course_code + " " + name + " is " + contact_phone

def get_contact_website(course_code):
    ans = DatabaseConnector.get_values("Select contact_website, course_name from course where "
                                                         'course.course_code = "' + course_code + '";')
    contact_website=ans[0][0]
    name=ans[0][1]
    return "The website of the contact person in " + course_code + " " + name + " is " + contact_website

def get_course_name(course_code):
    ans = DatabaseConnector.get_values('Select course_name from course where course.course_code = "' + course_code
                                       + '";')
    course_name=ans[0][0]
    return "The course name is " + course_code + " " + course_name

def get_credit(course_code):
    ans= DatabaseConnector.get_values("Select credit, course_name from course where course.course_code = \"" +
                                                course_code + "\" ;")
    credit=ans[0][0]
    name=ans[0][1]
    return "The course " + course_code + " " + name + " is " + credit + " credits."

def get_url(course_code):
    ans = DatabaseConnector.get_values("Select url, course_name from course where course.course_code = \""+
                                             course_code + "\" ;")
    url=ans[0][0]

    if url == "null":
        return "Course url not available."
    else:
        return url

def get_prereq_knowledge(course_code):
    ans = DatabaseConnector.get_values("Select prereq_knowledge, course_name from course where course.course_code"+
                                                " = \"" + course_code + "\" ;")
    prereq=ans[0][0]

    if prereq == "null":
        return "Prerequisite knowledge is not available for this course."
    else:
        return prereq

def get_course_content(course_code):
    ans = DatabaseConnector.get_values("Select course_content, course_name from course where" +
                                                        " course.course_code = \"" + course_code + "\" ;")
    course_content=ans[0][0]
    return course_content

def get_course_material(course_code):
    course_material = DatabaseConnector.get_values("Select course_material, course_name from course where " +
                                                         "course_code = \"" + course_code + "\";")
    return course_material[0][0]

def get_teaching_form(course_code):
    teaching_form  = DatabaseConnector.get_values("Select teaching_form, course_name from course where course_code =\""
                                                  + course_code +"\";")
    return teaching_form[0][0]

def get_exercise_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_exercise as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")
    return(ans)
    score = str(ans[0][1])
    required = str(ans[0][2])
    course_name= ans[0][3]
    return "You have done " + score + " out of " + required + " exercises in " + course_code + " " + course_name+"."

def get_project_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_project as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")
    score = str(ans[0][1])
    required = str(ans[0][2])
    course_name= ans[0][3]
    return "You have done " + score + " out of " + required + " projects in " + course_code + " " + course_name+"."

def get_lab_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_lab as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")
    score = str(ans[0][1])
    required = str(ans[0][2])
    course_name= ans[0][3]
    return "You have done " + score + " out of " + required + " lab in " + course_code + " " + course_name+"."


#Må lage def for get_term