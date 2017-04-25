from database import DatabaseConnector
from datetime import datetime, date
import time
# todo: make possible for nontype fields

"""
Functions that returs strings that the user will see is listed under here
"""


def get_exam_date(course_code):
    ans = DatabaseConnector.get_values("Select exam_date, course_name from course where "
                                       "course.course_code = \"" + course_code + "\";")

    date = ans[0][0]
    name = ans[0][1]

    if date == "null":
        if not "Written examination" in get_assessment_form(course_code):
            return "No date available because there is another assessment form."
        else:
            return "No exam data available."
    else:
        return "Exam date in " + course_code + " " + name + " is " + format_date_date(date)
        # todo: add reason if field is empty


def get_exam_dates(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course where "
                                       "user_has_course.username = \"" + username + "\";")

    string = ""
    for course_code in ans:
        string += course_code[0] + ": " + get_exam_date(course_code[0]) + "\n\n"

    return string


def get_course_codes(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course where user_has_course.username = \"" + username + "\"")

    string = ""
    for course_code in ans:
        string += course_code[0] + "\n"

    return string


def get_course_names(username):
    list = get_course_codes_list(username)

    string = ""
    for course_code in list:
        ans = DatabaseConnector.get_values(
            "Select course_name from course where course_code = \"" + course_code[0] + "\";")

        course_name = ans[0][0]
        string += course_name + "\n"

    return string


def get_number_of_courses(username):
    list = get_course_codes_list(username)

    return "You have " + str(len(list)) + " courses."


def get_assessment_form(course_code):
    ans = DatabaseConnector.get_values('Select assessment_form, course_name from course where '
                                       'course.course_code = "' + course_code + '";')
    assessment_form = ans[0][0]
    name = ans[0][1]
    return "Assessment form in " + course_code + " " + name + " is " + assessment_form


def get_contact_name(course_code):
    ans = DatabaseConnector.get_values("Select contact_name, course_name  from course where "
                                       "course.course_code = \"" + course_code + "\";")
    contact_name = ans[0][0]
    name = ans[0][1]
    return "The name of the contact person in " + course_code + " " + name + " is " + contact_name


def get_contact_mail(course_code):
    ans = DatabaseConnector.get_values("Select contact_mail, course_name from course where course.course_code = \""
                                       + course_code + "\";")
    contact_mail = ans[0][0]
    name = ans[0][1]
    return "The mail address of the contact person in " + course_code + " " + name + " is " + contact_mail


def get_contact_office(course_code):
    ans = DatabaseConnector.get_values("Select contact_office, course_name from course where course.course_code = \""
                                       + course_code + "\";")
    contact_office = ans[0][0]
    name = ans[0][1]

    if contact_office == "null":
        return "There is no existing office address in " + course_code + " " + name
    else:
        return "The office address of the contact person in " + course_code + " " + name + " is " + contact_office


def get_contact_phone(course_code):
    print(course_code)
    ans = DatabaseConnector.get_values("Select contact_phone, course_name from course where course.course_code = \""
                                       + course_code + "\";")
    contact_phone = ans[0][0]
    name = ans[0][1]

    if contact_phone == "null":
        return "There is no phone number available in " + course_code + " " + name
    else:
        return "The phone number of the contact person in " + course_code + " " + name + " is " + contact_phone


def get_contact_(course_code):
    ans = DatabaseConnector.get_values("Select contact_website, course_name from course where "
                                       'course.course_code = "' + course_code + '";')
    contact_website = ans[0][0]
    name = ans[0][1]
    return "The website of the contact person in " + course_code + " " + name + " is " + contact_website


def get_course_name(course_code):
    ans = DatabaseConnector.get_values('Select course_name from course where course.course_code = "' + course_code
                                       + '";')
    course_name = ans[0][0]
    return "The course name is " + course_code + " " + course_name


def get_credit(course_code):
    ans = DatabaseConnector.get_values("Select credit, course_name from course where course.course_code = \"" +
                                       course_code + "\" ;")
    credit = ans[0][0]
    name = ans[0][1]
    return "The course " + course_code + " " + name + " is " + credit + " credits."


def get_url(course_code):
    ans = DatabaseConnector.get_values("Select url, course_name from course where course.course_code = \"" +
                                       course_code + "\" ;")
    url = ans[0][0]

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
    ans = DatabaseConnector.get_values("Select prereq_knowledge, course_name from course where course.course_code" +
                                       " = \"" + course_code + "\" ;")
    prereq = ans[0][0]

    if prereq == "null":
        return "Prerequisite knowledge is not available for this course."
    else:
        return prereq


def get_course_content(course_code):
    ans = DatabaseConnector.get_values("Select course_content, course_name from course where" +
                                       " course.course_code = \"" + course_code + "\" ;")
    course_content = ans[0][0]
    return course_content


def get_course_material(course_code):
    course_material = DatabaseConnector.get_values("Select course_material, course_name from course where " +
                                                   "course_code = \"" + course_code + "\";")
    return course_material[0][0]


def get_teaching_form(course_code):
    teaching_form = DatabaseConnector.get_values("Select teaching_form, course_name from course where course_code =\""
                                                 + course_code + "\";")
    return teaching_form[0][0]


def get_exercise_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_exercise as S, course as C where S.course_code = \"" + course_code + "\" "
                                                                                                                    "and S.course_code = C.course_code and S.username = \"" + username + "\" group by "
                                                                                                                                                                                         "S.username ;")
    try:
        score = str(ans[0][1])
        course_name = ans[0][3]
        required = str(ans[0][2])
        if required == "None":
            return "You have done " + score + " exercises in " + course_code + " " + course_name + "."
        else:
            return "You have done " + score + " out of " + required + " required exercises in " + course_code + " " + course_name + "."
    except:
        return "Sorry, I could not get the exercise status."


def get_exercise_scheme_approval(course_code, username):

    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_exercise as S, course as C where S.course_code = \"" + course_code + "\" "
                                        "and S.course_code = C.course_code and S.username = \"" + username + "\" group by ""S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name=ans[0][3]
        if required == "None":
            if int(score) >= 8:
                return "Yes, you have completed the exercise scheme in " + course_code + " " + course_name + "."
            else:
                return "No, you have done " + score + " out of " + str(8) + " required exercises in " + course_code + " " + course_name + "."

        if int(score) >= required:
            return "Yes, you have completed all the required assignments!"
        else:
            return "No, you have done " + score + " out of " + required + " required exercises in " + course_code + " " + course_name + "."
    except:
        return "Sorry, I don't know how many exercises is required."

def get_exercises_left(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_exercise as S, course as C where S.course_code = \"" + course_code + "\" "
                                                                                                                    "and S.course_code = C.course_code and S.username = \"" + username + "\" group by "
                                                                                                                                                                                         "S.username ;")

    try:
        score = str(ans[0][1])
        course_name = ans[0][3]
        required = str(ans[0][2])

        if required == "None":
            left = str(8-int(score))
        else:
            left = str(required - int(score))

        if int(left) >= 0:
            return "You have " + left + " exercises left in " + course_code + " " + course_name + "."
        else:
            return "You don't have any exercises left in " + course_code + " " + course_name + "."

    except:
        return "You haven't done any exercises in this course yet."



def get_project_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_project as S, course as C where S.course_code = \"" + course_code + "\" "
                                                                                                                   "and S.course_code = C.course_code and S.username = \"" + username + "\" group by "
                                                                                                                                                                                        "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name = ans[0][3]
        return "You have done " + score + " out of " + required + " projects in " + course_code + " " + course_name + "."
    except:
        return "Sorry, i could not get the project status."


def get_lab_status(course_code, username):
    ans = DatabaseConnector.get_values("Select S.username, S.total_score, S.req_score, C.course_name from "
                                       "status_lab as S, course as C where S.course_code = \"" + course_code + "\" "
                                                                                                               "and S.course_code = C.course_code and S.username = \"" + username + "\" group by "
                                                                                                                                                                                    "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name = ans[0][3]
        return "You have done " + score + " out of " + required + " lab in " + course_code + " " + course_name + "."
    except:
        return "Sorry, i could not get the lab status."


def get_next_event(username):
    ans = DatabaseConnector.get_values("Select U.category, U.date_time, U.room, U.course_code, C.course_name "
                                       "from user_event as U, course as C "
                                       "where U.username = \"" + username + "\" and U.course_code = C.course_code order by date_time LIMIT 1")
    try:
        description = ans[0][0]
        date = ans[0][1]
        room = ans[0][2]
        course_name = ans[0][4]
        return "Your next event is a " + description + " in the course " + course_name + " in " + room + ", " + format_date(date)
    except:
        return "I could not find any events."


# todo: test this method
def get_next_assignment(username):
    ans = DatabaseConnector.get_values("Select A.title, A.deadline, course.course_name "
                                       " from user_assignment as A "
                                       "JOIN course on A.course_code = course.course_code "
                                       " where (A.username = \"" + username + "\") and (deadline BETWEEN Date('now') AND DATE('now', '+365 days')) "
                                                                              " order by deadline ASC "
                                                                              " LIMIT 1;")

    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "Your next assignment delivery is " + title + " which is due " + format_date(date) + ", in the course " + course_name + "."
    except:
        return "I could not find any assignments."


def get_days_until_first_exam(username):
    course_list = get_course_codes_list(username)



    if len(course_list) == 0:
        return "Sorry, i cannot find the number of days until your exam."

    dates = []

    for course_code in course_list:
        ans = DatabaseConnector.get_values("Select exam_date, course_name from course where "
                                           "course.course_code = \"" + course_code[0] + "\" and exam_date > Date('now');")

        try:
            date = ans[0][0]
            course_name = ans[0][1]
        except:
            continue

        if date == "null" or course_name == "null":
            continue
        else:
            time1 = time.strptime(date, "%Y-%m-%d")
            dates.append((time1, course_name))

    closestDate = sorted(dates, key=lambda tup: tup[0])

    from time import mktime
    from datetime import datetime

    dt = datetime.fromtimestamp(mktime(closestDate[0][0]))

    days_to_exam = (dt - datetime.now())

    return "There is " + str(days_to_exam.days) + " days to your first exam in " + closestDate[0][1]


def get_today_assignments(username):
    ans = DatabaseConnector.get_values("Select A.title, A.deadline, course.course_name "
                                       " from user_assignment as A "
                                       "JOIN course on A.course_code = course.course_code "
                                       " where (A.username = \"" + username + "\") and (deadline BETWEEN Date('now') AND DATE('now', '+1 days')) "
                                                                              " order by deadline ASC ")

    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "You have an assignment " + title + " in course " + course_name + ", that should be delivered today at " + format_date(date)
    except:
        return "I could not find any assignments that should be delivered today."

def get_tomorrow_assignments(username):
        ans = DatabaseConnector.get_values("Select A.title, A.deadline, course.course_name "
                                           " from user_assignment as A "
                                           "JOIN course on A.course_code = course.course_code "
                                           " where (A.username = \"" + username + "\") and (deadline BETWEEN Date('now', '+1 days') AND DATE('now', '+2 days')) "
                                                                                  " order by deadline ASC ")

        try:
            title = ans[0][0]
            date = ans[0][1]
            course_name = ans[0][2]
            return "You have an assignment " + title + " in course " + course_name + ", that should be delivered tomorrow at " + \
                   format_date_datetime(date)
        except:
            return "I could not find any assignments that should be delivered tomorrow."

def get_today_events(username):
    ans = DatabaseConnector.get_values("Select A.category, A.date_time, course.course_name "
                                       " from user_event as A "
                                       "JOIN course on A.course_code = course.course_code "
                                       " where (A.username = \"" + username + "\") and (date_time BETWEEN Date('now') AND DATE('now', '+1 days')) "
                                                                              " order by date_time ASC ")

    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "You have an event " + title + " in course " + course_name + ", today at " + \
               format_date_datetime(date)
    except:
        return "I could not find any events today."

def get_tomorrow_events(username):
    ans = DatabaseConnector.get_values("Select A.category, A.date_time, course.course_name "
                                       " from user_event as A "
                                       "JOIN course on A.course_code = course.course_code "
                                       " where (A.username = \"" + username + "\") and (date_time BETWEEN Date('now', '+1 days') AND DATE('now', '+2 days')) "
                                                                              " order by date_time ASC ")

    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "You have an event " + title + " in course " + course_name + ", " + \
               format_date_datetime(date)
    except:
        return "I could not find any events for tomorrow."


def get_this_weeks_assignments(username):
    # Lists all the assignments that should be done this week


    ans = DatabaseConnector.get_values("Select A.title, A.deadline, C.course_name "
                                       "from user_assignment as A, course as C "
                                       "where (A.username = \"" + username + "\") and (A.course_code = C.course_code) and (deadline BETWEEN Date('now', 'localtime', 'weekday 0', '-7 days') AND date('now', 'localtime', 'weekday 0')) order by deadline ASC")

    try:

        if len(ans) == 0:
            return "You dont have any assignments this week."

        string_builder = "This weeks assignments:\n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]

            string_builder += title + " which is due " + format_date_datetime(date) + ", in the course " + course_name + ".\n"

        return string_builder
    except:
        return "You dont have any assignments this week."


def get_this_weeks_events(username):
    ans = DatabaseConnector.get_values(
        "Select user_event.course_code, user_event.date_time, course.course_name, user_event.room, user_event.category "
        "from user_event "
        "JOIN course on user_event.course_code = course.course_code "
        "where(user_event.username = \"" + username + "\") and (date_time BETWEEN Date('now', 'localtime', 'weekday 0', '-7 days') AND date('now', 'localtime', 'weekday 0')) order by date_time ASC ")

    try:

        if len(ans) == 0:
            return "You dont have any events this week."

        string_builder = "This weeks events:\n"
        for i in range(0, len(ans)):
            date = ans[i][1]
            course_name = ans[i][2]
            room = ans[i][3]
            category = ans[i][4]

            string_builder += category + " in " + room + " in " + course_name + " " + format_date(date) + "\n"

        return string_builder
    except:
        return "You dont have any events this week."


def get_next_weeks_events(username):
    ans = DatabaseConnector.get_values(
        "Select user_event.course_code, user_event.date_time, course.course_name, user_event.room, user_event.category "
        "from user_event "
        "JOIN course on user_event.course_code = course.course_code "
        "where(user_event.username = \"" + username + "\") and (date_time BETWEEN Date('now', 'localtime', 'weekday 1') AND date('now', 'localtime', 'weekday 0', '+8 days')) order by date_time ASC ")

    try:

        if len(ans) == 0:
            return "You dont have any events next week."

        string_builder = "Next weeks events:\n"
        for i in range(0, len(ans)):
            date = ans[i][1]
            course_name = ans[i][2]
            room = ans[i][3]
            category = ans[i][4]

            string_builder += category + " in " + room + " in " + course_name + " " + format_date(date) + "\n"

        return string_builder
    except:
        return "You dont have any events next week."


def get_next_weeks_assignments(username):
    # Lists all the assignments that should be done by next week

    ans = DatabaseConnector.get_values("Select A.title, A.deadline, C.course_name "
                                       "from user_assignment as A, course as C "
                                       "where (A.username = \"" + username + "\") and (A.course_code = C.course_code) and (deadline BETWEEN Date('now', 'localtime', 'weekday 0') AND date('now', 'localtime', 'weekday 0', '+8 days')) order by deadline ASC")

    try:

        if len(ans) == 0:
            return "You dont have any assignments next week."

        string_builder = "Next weeks assignments:\n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]

            string_builder += title + " which is due " + format_date_datetime(date) + ", in the course " + course_name + ".\n"

        return string_builder
    except:
        return "You dont have any assignments next week."


def get_next_week_schedule(username):
    return get_next_weeks_assignments(username) + "\n" + get_next_weeks_events(username)


def get_this_week_schedule(username):
    return get_this_weeks_assignments(username) + "\n" + get_this_weeks_events(username)



def get_ical_itslearning(username):
    ans = DatabaseConnector.get_values("Select user.ical_itslearning from user where user.username = \"" + username + "\"")

    url = ""
    try:
        url = ans[0][0]
        return "https://www.google.com/calendar/render?cid=" + url
    except:
        return "There was no ical link for you."



"""
Functions that returns other types and is used as helper methods is listed here
"""


def get_course_codes_list(username):
    ans = DatabaseConnector.get_values("Select course_code from user_has_course WHERE user_has_course.username =  \"" + username + "\"")
    print(ans)
    course_codes = []
    for course_code in ans:
        course_codes.append(course_code)

    return course_codes


def format_date_datetime(datetime: str):
    time1 = time.strptime(datetime, '%Y-%m-%d %H:%M:%S')
    datestring = time.strftime('%A %d %B %H:%M:%S', time1)

    return datestring


def format_date_date(date: str):
    time1 = time.strptime(date, '%Y-%m-%d')
    datestring = time.strftime('%A %d %B', time1)

    return datestring


def get_users() -> list:
    ans = DatabaseConnector.get_values("Select * from user ORDER BY registry_date DESC ")

    return ans

def delete_user():
    ans = DatabaseConnector.get_values("delete from user")

print(get_exercises_left("TKT4123", "marihl"))
