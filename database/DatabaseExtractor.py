from database import DatabaseConnector
import time

"""
Functions that returs strings that the user will see is listed under here
"""


def get_exam_date(course_code):
    """
    Returns the exam date for a subject
    :param course_code: the subjects course code
    :return: String with exam date that is presented to the user
    """
    ans = DatabaseConnector.get_values("SELECT exam_date, course_name FROM course WHERE "
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


def get_exam_dates(username):
    """
    Returns a list of exam dates for a subject
    :param username: the users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT course_code FROM user_has_course WHERE "
                                       "user_has_course.username = \"" + username + "\";")

    string = ""
    for course_code in ans:
        string += course_code[0] + ": " + get_exam_date(course_code[0]) + "\n\n"

    return string


def get_course_codes(username):
    """
    Returns a list of course codes that a user has
    :param username: the users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values(
        "SELECT course_code FROM user_has_course WHERE user_has_course.username = \"" + username + "\"")

    string = ""
    for course_code in ans:
        string += course_code[0] + "\n"

    return string


def get_course_names(username):
    """
    Returns a list of course names that a user has
    :param username: the users username
    :return: String that is presented to the user
    """

    list = get_course_codes_list(username)

    string = ""
    for course_code in list:
        ans = DatabaseConnector.get_values(
            "SELECT course_name FROM course WHERE course_code = \"" + course_code[0] + "\";")

        course_name = ans[0][0]
        string += course_name + "\n"

    return string


def get_number_of_courses(username):
    """
    Returns the number of courses that a user has
    :param username: the users username
    :return: String that is presented to the user
    """
    list = get_course_codes_list(username)

    return "You have " + str(len(list)) + " courses."


def get_assessment_form(course_code):
    """
    Returns the assessment form for a course
    :param course_code: the courses course code
    :return: String that is presented to the user
    """
    ans = DatabaseConnector.get_values('SELECT assessment_form, course_name FROM course WHERE '
                                       'course.course_code = "' + course_code + '";')
    assessment_form = ans[0][0]
    name = ans[0][1]
    return "Assessment form in " + course_code + " " + name + " is " + assessment_form


def get_contact_name(course_code):
    """
    Returns the contact name to the contact person in a course
    :param course_code: the courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT contact_name, course_name  FROM course WHERE "
                                       "course.course_code = \"" + course_code + "\";")
    contact_name = ans[0][0]
    name = ans[0][1]
    return "The name of the contact person in " + course_code + " " + name + " is " + contact_name


def get_contact_mail(course_code):
    """
    Returns the mail to the contact person in a course
    :param course_code: the courses course code
    :return: String containing mail that is presented to the user
    """
    ans = DatabaseConnector.get_values("SELECT contact_mail, course_name FROM course WHERE course.course_code = \""
                                       + course_code + "\";")
    contact_mail = ans[0][0]
    name = ans[0][1]
    return "The mail address of the contact person in " + course_code + " " + name + " is " + contact_mail


def get_contact_office(course_code):
    """
    Returns the office to the contact person in a course
    :param course_code: the courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT contact_office, course_name FROM course WHERE course.course_code = \""
                                       + course_code + "\";")
    contact_office = ans[0][0]
    name = ans[0][1]

    if contact_office == "null":
        return "There is no existing office address in " + course_code + " " + name
    else:
        return "The office address of the contact person in " + course_code + " " + name + " is " + contact_office


def get_contact_phone(course_code):
    """
    Returns the phone number to the contact person in a course
    :param course_code: the courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT contact_phone, course_name FROM course WHERE course.course_code = \""
                                       + course_code + "\";")
    contact_phone = ans[0][0]
    name = ans[0][1]

    if contact_phone == "null":
        return "There is no phone number available in " + course_code + " " + name
    else:
        return "The phone number of the contact person in " + course_code + " " + name + " is " + contact_phone


def get_contact_website(course_code):
    """
    Returns the website for a contact 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT contact_website, course_name FROM course WHERE "
                                       'course.course_code = "' + course_code + '";')
    contact_website = ans[0][0]
    name = ans[0][1]
    return "The website of the contact person in " + course_code + " " + name + " is " + contact_website


def get_course_name(course_code):
    """
    Returns the course name for a course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values('SELECT course_name FROM course WHERE course.course_code = "' + course_code
                                       + '";')
    course_name = ans[0][0]
    return "The course name is " + course_code + " " + course_name


def get_credit(course_code):
    """
    Returns the amount of credit for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT credit, course_name FROM course WHERE course.course_code = \"" +
                                       course_code + "\" ;")
    credit = ans[0][0]
    name = ans[0][1]
    return "The course " + course_code + " " + name + " is " + credit + " credits."


def get_url(course_code):
    """
    Returns the url for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT url, course_name FROM course WHERE course.course_code = \"" +
                                       course_code + "\" ;")
    url = ans[0][0]

    if url == "null":
        return "Course url not available."
    else:
        return url


def get_term(course_code):
    """
    Returns the term that a given course is in
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT term FROM course WHERE course.course_code = \"" + course_code + "\"")

    term = ans[0][0]

    if term == "null":
        return "Term is not available."
    else:
        return term


def get_prereq_knowledge(course_code):
    """
    Returns the prerequisite knowledge for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT prereq_knowledge, course_name FROM course WHERE course.course_code" +
                                       " = \"" + course_code + "\" ;")
    prereq = ans[0][0]

    if prereq == "null":
        return "Prerequisite knowledge is not available for this course."
    else:
        return prereq


def get_course_content(course_code):
    """
    Returns the amount of credit for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT course_content, course_name FROM course WHERE" +
                                       " course.course_code = \"" + course_code + "\" ;")
    course_content = ans[0][0]
    return course_content


def get_course_material(course_code):
    """
    Returns the course material for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """

    course_material = DatabaseConnector.get_values("SELECT course_material, course_name FROM course WHERE " +
                                                   "course_code = \"" + course_code + "\";")
    return course_material[0][0]


def get_teaching_form(course_code):
    """
    Returns the teaching form for a given course 
    :param course_code: courses course code
    :return: String that is presented to the user
    """


    teaching_form = DatabaseConnector.get_values("SELECT teaching_form, course_name FROM course WHERE course_code =\""
                                                 + course_code + "\";")
    return teaching_form[0][0]


def get_exercise_status(course_code, username):
    """
    Returns the exercise status containing how many done out of required for a given course 
    :param course_code: courses course code
    :param username: users username
    :return: String that is presented to the user
    """


    ans = DatabaseConnector.get_values("SELECT S.username, S.total_score, S.req_score, C.course_name FROM "
                                       "status_exercise AS S, course AS C WHERE S.course_code = \"" + course_code + "\" "
                                                                                                                    "and S.course_code = C.course_code AND S.username = \"" + username + "\" GROUP BY "
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
    """
    Returns if the user has done all out all req
    :param course_code: courses course code
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT S.username, S.total_score, S.req_score, C.course_name FROM "
                                       "status_exercise AS S, course AS C WHERE S.course_code = \"" + course_code + "\" "
                                                                                                                    "and S.course_code = C.course_code AND S.username = \"" + username + "\" GROUP BY ""S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name = ans[0][3]
        if required == "None":
            if int(score) >= 8:
                return "Yes, you have completed the exercise scheme in " + course_code + " " + course_name + "."
            else:
                return "No, you have done " + score + " out of " + str(
                    8) + " required exercises in " + course_code + " " + course_name + "."

        if int(score) >= required:
            return "Yes, you have completed all the required assignments!"
        else:
            return "No, you have done " + score + " out of " + required + " required exercises in " + course_code + " " + course_name + "."
    except:
        return "Sorry, I don't know how many exercises is required."


def get_exercises_left(course_code, username):
    """
    Returns the amount of exercises left for a given course 
    :param course_code: courses course code
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT S.username, S.total_score, S.req_score, C.course_name FROM "
                                       "status_exercise AS S, course AS C WHERE S.course_code = \"" + course_code + "\" "
                                                                                                                    "and S.course_code = C.course_code AND S.username = \"" + username + "\" GROUP BY "
                                                                                                                                                                                         "S.username ;")

    try:
        score = str(ans[0][1])
        course_name = ans[0][3]
        required = str(ans[0][2])

        if required == "None":
            left = str(8 - int(score))
        else:
            left = str(required - int(score))

        if int(left) >= 0:
            return "You have " + left + " exercises left in " + course_code + " " + course_name + "."
        else:
            return "You don't have any exercises left in " + course_code + " " + course_name + "."

    except:
        return "You haven't done any exercises in this course yet."


def get_project_status(course_code, username):
    """
    Returns the project status for a given course 
    :param course_code: courses course code
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT S.username, S.total_score, S.req_score, C.course_name FROM "
                                       "status_project AS S, course AS C WHERE S.course_code = \"" + course_code + "\" "
                                                                                                                   "and S.course_code = C.course_code AND S.username = \"" + username + "\" GROUP BY "
                                                                                                                                                                                        "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name = ans[0][3]
        return "You have done " + score + " out of " + required + " projects in " + course_code + " " + course_name + "."
    except:
        return "Sorry, i could not get the project status."


def get_lab_status(course_code, username):
    """
    Returns the lab status for a given course 
    :param course_code: courses course code
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT S.username, S.total_score, S.req_score, C.course_name FROM "
                                       "status_lab AS S, course AS C WHERE S.course_code = \"" + course_code + "\" "
                                                                                                               "and S.course_code = C.course_code AND S.username = \"" + username + "\" GROUP BY "
                                                                                                                                                                                    "S.username ;")

    try:
        score = str(ans[0][1])
        required = str(ans[0][2])
        course_name = ans[0][3]
        return "You have done " + score + " out of " + required + " lab in " + course_code + " " + course_name + "."
    except:
        return "Sorry, i could not get the lab status."

def get_days_until_first_exam(username):
    """
    Returns the number of days until a users next exam
    :param username: users username
    :return: String that is presented to the user
    """

    course_list = get_course_codes_list(username)

    if len(course_list) == 0:
        return "Sorry, i cannot find the number of days until your exam."

    dates = []

    for course_code in course_list:
        ans = DatabaseConnector.get_values("SELECT exam_date, course_name FROM course WHERE "
                                           "course.course_code = \"" + course_code[
                                               0] + "\" AND exam_date > Date('now');")

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











def get_next_event(username):
    """
    Returns the next event that a user has 
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT U.category, U.date_time, U.room, U.course_code, U.course_code "
                                       "from user_event AS U "
                                       "WHERE (U.username = \"" + username + "\") AND (U.date_time BETWEEN Date('now') AND DATE('now', '+365 days')) "
                                                                              " ORDER BY U.date_time ASC "
                                                                              " LIMIT 1;")
    try:
        category = ans[0][0]
        date = ans[0][1]
        room = ans[0][2]
        course_name = ans[0][4]
        return "Your next event is a " + category + " in the course " + course_name + " in " + room + ", " + format_date_datetime(date)
    except:
        return "I could not find any events."


def get_next_assignment(username):
    """
    Returns the next assignment that a user has 
    :param username: users username
    :return: String that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT A.title, A.deadline, course.course_name "
                                       " FROM user_assignment AS A "
                                       "JOIN course ON A.course_code = course.course_code "
                                       " WHERE (A.username = \"" + username + "\") AND (deadline BETWEEN Date('now') AND DATE('now', '+365 days')) "
                                                                              " ORDER BY deadline ASC "
                                                                              " LIMIT 1;")

    try:
        title = ans[0][0]
        date = ans[0][1]
        course_name = ans[0][2]
        return "Your next assignment delivery is " + title + " which is due " + format_date_datetime(
            date) + ", in the course " + course_name + "."
    except:
        return "I could not find any assignments."


def get_today_assignments(username):
    """
    Returns assignments that have to be delivered today
    :param username: users username
    :return: A string containing assignments that has to be delivered today that is presented to the user
    """


    ans = DatabaseConnector.get_values("SELECT A.title, A.deadline, course.course_name "
                                       " FROM user_assignment AS A "
                                       "JOIN course ON A.course_code = course.course_code "
                                       " WHERE (A.username = \"" + username + "\") AND (deadline BETWEEN Date('now') AND DATE('now', '+1 days')) "
                                                                              " ORDER BY deadline ASC ")
    if len(ans) == 0:
        return "I could not find any assignments that should be delivered today."
    try:
        string_builder = "Todays assignments: \n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]
            string_builder += "- " + title + " in course " + course_name + ", that should be delivered today at " + format_date_datetime(
            date) + "\n"

        return string_builder
    except:
        return "I could not find any assignments that should be delivered today."


def get_tomorrow_assignments(username):
    """
    Returns assignments that has to be delivered tomorrow
    :param username: users username
    :return: A string containing assignments that has to be delivered tomorrow
    """

    ans = DatabaseConnector.get_values("SELECT A.title, A.deadline, course.course_name "
                                       " FROM user_assignment AS A "
                                       "JOIN course ON A.course_code = course.course_code "
                                       " WHERE (A.username = \"" + username + "\") AND (deadline BETWEEN Date('now', '+1 days') AND DATE('now', '+2 days')) "
                                                                              " ORDER BY deadline ASC ")

    try:
        string_builder = "Tomorrow assignments: \n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]
            string_builder += "- " + title + " in course " + course_name + ", that should be delivered tomorrow at " + \
               format_date_datetime(date) + "\n"
        return string_builder

    except:
        return "I could not find any assignments that should be delivered tomorrow."



def get_today_events(username):
    """
    Returns events that is happening today
    :param username: users username
    :return: A string containing events today that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT A.category, A.date_time, course.course_name "
                                       " FROM user_event AS A "
                                       "JOIN course ON A.course_code = course.course_code "
                                       " WHERE (A.username = \"" + username + "\") AND (date_time BETWEEN Date('now') AND DATE('now', '+1 days')) "
                                                                              " ORDER BY date_time ASC ")

    try:
        string_builder = "Todays events: \n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]
            string_builder += "- " + title + " in course " + course_name + ", today at " + \
               format_date_datetime(date) + "\n"
        return string_builder
    except:
        return "I could not find any events today."


def get_tomorrow_events(username):
    """
    Returns events that is happening tomorrow
    :param username: users username
    :return: A string containing events tomorrow that is presented to the user
    """

    ans = DatabaseConnector.get_values("SELECT A.category, A.date_time, course.course_name, A.room "
                                       " FROM user_event AS A "
                                       "JOIN course ON A.course_code = course.course_code "
                                       " WHERE (A.username = \"" + username + "\") AND (date_time BETWEEN Date('now', '+1 days') AND DATE('now', '+2 days')) "
                                                                              " ORDER BY date_time ASC ")

    try:
        string_builder = "Tomorrows events: \n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]
            room = ans[i][3]
            string_builder += "- " + title + " in course " + course_name + ", "  + format_date_datetime(date) + " in " + room + "\n"
        return string_builder
    except:
        return "I could not find any events for tomorrow."



def get_this_weeks_assignments(username):
    """
    Returns a list of this weeks assignments 
    :param username: users username
    :return: String containing schedule that is presented to the user
    """


    ans = DatabaseConnector.get_values("SELECT A.title, A.deadline, C.course_name "
                                       "from user_assignment AS A, course AS C "
                                       "where (A.username = \"" + username + "\") AND (A.course_code = C.course_code) AND (deadline BETWEEN Date('now', 'localtime', 'weekday 0', '-7 days') AND date('now', 'localtime', 'weekday 0')) ORDER BY deadline ASC")

    try:

        if len(ans) == 0:
            return "You dont have any assignments this week."

        string_builder = "This weeks assignments:\n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]

            string_builder += "- " + title + " which is due " + format_date_datetime(
                date) + ", in the course " + course_name + ".\n"

        return string_builder
    except:
        return "You dont have any assignments this week."



def get_this_weeks_events(username):
    """
    Returns a list of this weeks event
    :param username: users username
    :return: String containing list of events that is presented to the user
    """


    ans = DatabaseConnector.get_values(
        "SELECT user_event.course_code, user_event.date_time, user_event.room, user_event.category "
        "from user_event "
        "where(user_event.username = \"" + username + "\") AND (date_time BETWEEN Date('now', 'localtime', 'weekday 0', '-7 days') AND date('now', 'localtime', 'weekday 0', '+1 days')) ORDER BY date_time ASC ")

    try:

        if len(ans) == 0:
            return "You dont have any events this week."

        string_builder = "This weeks events:\n"
        for i in range(0, len(ans)):
            date = ans[i][1]
            course_name = ans[i][2]
            room = ans[i][3]
            category = ans[i][4]

            string_builder += "- " + category + " in " + room + " in " + course_name + " " + format_date_datetime(date) + "\n"

        return string_builder
    except:
        return "You dont have any events this week."

def get_next_weeks_events(username):
    """
    Gets next weeks events
    :param username: users username
    :return: String containing next weeks events that is presented to the user
    """

    ans = DatabaseConnector.get_values(
        "SELECT user_event.course_code, user_event.date_time, course.course_name, user_event.room, user_event.category "
        "from user_event "
        "JOIN course ON user_event.course_code = course.course_code "
        "where(user_event.username = \"" + username + "\") AND (date_time BETWEEN Date('now', 'localtime', 'weekday 1') AND date('now', 'localtime', 'weekday 0', '+8 days')) ORDER BY date_time ASC ")

    try:

        if len(ans) == 0:
            return "You dont have any events next week."

        string_builder = "Next weeks events:\n"
        for i in range(0, len(ans)):
            date = ans[i][1]
            course_name = ans[i][2]
            room = ans[i][3]
            category = ans[i][4]

            string_builder += "- " + category + " in " + room + " in " + course_name + " " + format_date_datetime(date) + "\n"

        return string_builder
    except:
        return "You dont have any events next week."

def get_next_weeks_assignments(username):
    """
    Gets next weeks assignments
    :param username: users username
    :return: String containing next weeks assignments to the user
    """

    ans = DatabaseConnector.get_values("SELECT A.title, A.deadline, C.course_name "
                                       "from user_assignment AS A, course AS C "
                                       "where (A.username = \"" + username + "\") AND (A.course_code = C.course_code) AND (deadline BETWEEN Date('now', 'localtime', 'weekday 0', '+1 days') AND date('now', 'localtime', 'weekday 0', '+8 days')) ORDER BY deadline ASC")

    try:

        if len(ans) == 0:
            return "You dont have any assignments next week."

        string_builder = "Next weeks assignments:\n"
        for i in range(0, len(ans)):
            title = ans[i][0]
            date = ans[i][1]
            course_name = ans[i][2]

            string_builder += "- " + title + " which is due " + format_date_datetime(
                date) + ", in the course " + course_name + ".\n"

        return string_builder
    except:
        return "You dont have any assignments next week."

def get_next_week_schedule(username):
    """
    Next weeks schedule contains both events and assignments for next week
    :param username: users username
    :return: String containing schedule that is presented to the user
    """
    return get_next_weeks_assignments(username) + "\n" + get_next_weeks_events(username)

def get_this_week_schedule(username):
    """
    This weeks schedule contains both events and assignments for this week
    :param username: users username
    :return: String containing schedule that is presented to the user
    """
    return get_this_weeks_assignments(username) + "\n" + get_this_weeks_events(username)

def get_ical_itslearning(username):
    """
    Returns a link that users can subscribe to
    :param username: users username
    :return: a link that is presented to the user
    """

    ans = DatabaseConnector.get_values(
        "SELECT user.ical_itslearning FROM user WHERE user.username = \"" + username + "\"")

    url = ""
    try:
        url = ans[0][0]
        return "https://www.google.com/calendar/render?cid=" + url
    except:
        return "There was no ical link for you."


"""
Functions that returns other types than strings presented to the user and is used as helper methods is listed here
"""


def get_course_codes_list(username):
    """
    Returns a list of course codes
    :param username: users username
    :return: a list of course codes
    """

    ans = DatabaseConnector.get_values(
        "SELECT course_code FROM user_has_course WHERE user_has_course.username =  \"" + username + "\"")
    course_codes = []
    for course_code in ans:
        course_codes.append(course_code)

    return course_codes


def format_date_datetime(datetime: str):
    """
    Formats the date to a date that is more understandable by a human
    :param datetime: date on on the format e.g 2017-02-14 12:12:13
    :return: date on the format: Monday 12 January 12:12:13
    """

    time1 = time.strptime(datetime, '%Y-%m-%d %H:%M:%S')
    datestring = time.strftime('%A %d %B %H:%M', time1)

    return datestring


def format_date_date(date: str):
    """
    Formats the date to a date that is more understandable by a human
    :param date: date on on the format e.g 2017-02-14
    :return: date on the format: Monday 12 January
    """

    time1 = time.strptime(date, '%Y-%m-%d')
    datestring = time.strftime('%A %d %B', time1)

    return datestring


def get_users() -> list:
    """
    Gets all the users sorted DESCENDING by register date
    :return: a list with users and attributes
    """
    ans = DatabaseConnector.get_values("SELECT * FROM user ORDER BY registry_date DESC ")

    return ans


def delete_user():
    """
    Deletes all the users in the database
    :return: nothing
    """
    ans = DatabaseConnector.get_values("DELETE FROM user")
