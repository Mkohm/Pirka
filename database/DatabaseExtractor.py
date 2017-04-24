from database import DatabaseConnector
from datetime import datetime, date
#todo: make possible for nontype fields

"""
Functions that returs strings that the user will see is listed under here
"""


def get_exam_date(course_code):
    ans = DatabaseConnector.get_values("Select exam_date, course_name from course where "
                                               "course.course_code = \"" + course_code + "\";")

    date = ans[0][0]
    name=ans[0][1]

    if date == "null":
        if not "Written examination" in get_assessment_form(course_code):
            return "No date available because there is another assessment form."
        else:
            return "No exam data available."
    else:
        return "Exam date in " + course_code + " " + name + " is " + date
    #todo: add reason if field is empty

def get_exam_dates(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course where "
                                       "user_has_course.username = \"" + username + "\";")

    string = ""
    for course_code in ans:
        string += course_code[0] + ": " + get_exam_date(course_code[0]) + "\n\n"

    return string

def get_course_codes(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course")

    string = ""
    for course_code in ans:
        string += course_code[0] + "\n"

    return string

def get_course_names(username):

    list = get_course_codes_list(username)

    string = ""
    for course_code in list:
        ans = DatabaseConnector.get_values("Select course_name from course where course_code = \"" + course_code[0] + "\";")

        course_name = ans[0][0]
        string += course_name + "\n"

    return string

def get_number_of_courses(username):

    list = get_course_codes_list(username)


    return "You have " + str(len(list)) + " courses."


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
    print(course_code)
    ans = DatabaseConnector.get_values("Select contact_phone, course_name from course where course.course_code = \""
                                                       + course_code + "\";")
    contact_phone=ans[0][0]
    name=ans[0][1]

    if contact_phone == "null":
        return "There is no phone number available in " + course_code + " " + name
    else:
        return "The phone number of the contact person in " + course_code + " " + name + " is " + contact_phone

def get_contact_(course_code):
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

def get_term(course_code):
    ans = DatabaseConnector.get_values("Select term from course where course.course_code = \"" + course_code + "\"")

    term = ans[0][0]

    if term == "null":
        return "Term is not available."
    else:
        return term



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


    try:
        score = str(ans[0][1])
        course_name= ans[0][3]
        required = str(ans[0][2])
        if required == "None":
            return "You have done " + score + " exercises in " + course_code + " " + course_name+"."
        else:
            return "You have done " + score + " out of " + required + " exercises in " + course_code + " " + course_name+"."
    except:
        return "null"

def get_exercises_left(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_exercise as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")


    try:
        score = ans[0][1]
        course_name= ans[0][3]
        required = ans[0][2]


        if required == "None":

            return "You have done " + str(score) + " exercises in " + course_code + " " + course_name+"."
        else:
            left = str(required - score)
            return "You have " + left + " exercises left in " + course_code + " " + course_name+"."
    except:
        return "You haven't done any exercises in this course yet."

def get_project_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_project as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name= ans[0][3]
        return "You have done " + score + " out of " + required + " projects in " + course_code + " " + course_name+"."
    except:
        return "null"

def get_lab_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_lab as S, course as C where S.course_code = \"" +course_code+"\" "
                                       "and S.course_code = C.course_code and S.username = \"" + username +"\" group by "
                                        "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name= ans[0][3]
        return "You have done " + score + " out of " + required + " lab in " + course_code + " " + course_name+"."
    except:
        return "null"

def get_next_event(username):
    ans = DatabaseConnector.get_values("Select U.category, U.date_time, U.room, U.course_code, C.course_name "
                                       "from user_event as U, course as C "
                                       "where U.username = \"" + username + "\" and U.course_code = C.course_code order by date_time LIMIT 1")
    try:
        description = ans[0][0]
        date = ans[0][1]
        room = ans[0][2]
        course_name = ans[0][4]
        return "Your next event is a " + description + " in the course " + course_name + " in " + room + ", " + date
    except:
        return "null"


# todo: fix this method, this method will return the latest assignment, not the next
def get_next_assignment(username):



    ans = DatabaseConnector.get_values("Select A.title, A.deadline, course.course_name "
                                        " from user_assignment as A "
                                        "JOIN course on A.course_code = course.course_code "
                                        " where (A.username = \"" + username + "\") and (deadline BETWEEN Date('now') AND DATE('now', 'weekday 0')) "
                                        " order by deadline ASC "
                                        " LIMIT 1;")


    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "Your next assignment delivery is " + title + " which is due " + date + ", in the course " + course_name + "."
    except:
        return "null"

def get_days_until_first_exam(username):

    course_list = get_course_codes_list(username)

    dates = []

    for course_code in course_list:
        ans = DatabaseConnector.get_values("Select exam_date, course_name from course where "
                                       "course.course_code = \"" + course_code[0] + "\";")


        date = ans[0][0]
        if date == "null":
            continue
        else:
            #dato = datetime.date(datetime.strptime("Jun 02, 2017", "%b %d, %Y"))
            dato = datetime.date(datetime.strptime(str(date).split(" ")[0][0:3] + " " + str(date).split(" ")[1] + " " + str(date).split(" ")[2], "%b %d, %Y"))
            dates.append(dato)

    closestDate = min(dates)

    days_to_exam = (closestDate - datetime.now().date())

    return "There is " + str(days_to_exam.days) + " days to your first exam."

def get_this_weeks_schedule(username):
    # Lists all the assignments that should be done this week


    ans = DatabaseConnector.get_values("Select A.title, A.deadline, C.course_name "
                                        "from user_assignment as A, course as C "
                                        "where (A.username = \"" + username + "\") and (A.course_code = C.course_code) and (deadline BETWEEN Date('now') AND DATE('now', 'weekday 0')) order by deadline ASC")

    print(ans)
    try:
        string_builder = "This weeks schedule:\n"
        for i in range(0, len(ans)):

            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]

            string_builder += title + " which is due " + date + ", in the course " + course_name + ".\n"

        return string_builder
    except:
        return "null"





def get_next_weeks_schedule(username):
    # Lists all the assignments that should be done by next week

    pass

def get_all_remaining_assignments(username):
    # Lists all the remaining assignments

    pass



"""
Functions that returns other types and is used as helper methods is listed here
"""

def get_course_codes_list(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course")

    course_codes = []
    for course_code in ans:
        course_codes.append(course_code)

    return course_codes



def get_users() -> list:
    ans = DatabaseConnector.get_values("Select * from user")

    return ans


print(get_this_weeks_schedule("mariukoh"))