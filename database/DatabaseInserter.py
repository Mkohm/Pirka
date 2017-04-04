from datetime import datetime

import requests

import database.DatabaseConnector

base_url = "http://www.ime.ntnu.no/api/course/en/"


def add_subject_data(course_code: str):
    """
    This method will get all the useful data from one course code
     - and is inserting this into the subject table in the database.
    :param course_code: The course code that all the data should be derived from
    :return: nothing
    """

    # Get data to work with
    data = get_data(course_code)

    course_name = get_course_name(data)
    exam_date = get_exam_date(data)
    assessment_form = get_assessment_form(data)
    contact_name = get_contact_name(data)
    contact_mail = get_contact_mail(data)
    contact_office = get_contact_office(data)
    contact_phone = get_contact_phone(data)
    credit = get_credit(data)
    url = get_url(data)
    course_content = get_course_content(data)
    course_material = get_course_material(data)
    teaching_form = get_teaching_form(data)
    prereq_knowledge = get_prereq_knowledge(data)
    term = get_term(data)

    # Adds the data to a list for insertion into the table
    data = []
    data.append(course_code)
    data.append(course_name)
    data.append(exam_date)
    data.append(assessment_form)
    data.append(contact_name)
    data.append(contact_mail)
    data.append(contact_office)
    data.append(contact_phone)
    data.append(credit)
    data.append(url)
    data.append(prereq_knowledge)
    data.append(course_content)
    data.append(course_material)
    data.append(teaching_form)
    data.append(term)

    # Adds the data to the table
    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `course_material`, `teaching_form`, `term`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            data)
    except:
        cursor.execute(
            "UPDATE `course` SET course_name = ?, exam_date = ?, assessment_form = ?, contact_name = ?, contact_mail = ?, contact_office = ?, contact_phone = ?, credit = ?, url = ?, prereq_knowledge = ?, course_content = ?, course_material = ?, teaching_form = ?, term = ? WHERE course_code = \"" + course_code + "\"",
            data[1:15])

    connection.commit()


def get_prereq_knowledge(data):
    value = ""
    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "ANBFORK"):
                index = i
        except:
            prereq_knowledge = "null"
    try:
        prereq_knowledge = data["course"]["infoType"][index]["text"]
    except:
        prereq_knowledge = "null"

    return prereq_knowledge


def get_course_content(data):
    value = ""
    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "INNHOLD"):
                index = i
        except:
            course_content = "null"
    try:
        course_content = data["course"]["infoType"][index]["text"]
    except:
        course_content = "null"

    return course_content


def get_teaching_form(data):
    value = ""
    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "LÆRFORM"):
                index = i
        except:
            teaching_form = "null"
    try:
        teaching_form = data["course"]["infoType"][index]["text"]
    except:
        teaching_form = "null"

    return teaching_form


def get_course_material(data):
    value = ""
    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "KURSMAT"):
                index = i
        except:
            course_material = "null"
    try:
        course_material = data["course"]["infoType"][index]["text"]
    except:
        course_material = "null"

    return course_material


def get_url(data):
    value = ""
    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "E-URL"):
                index = i
        except:
            url = "null"
    try:
        url = data["course"]["infoType"][index]["text"]
    except:
        url = "null"

    return url


def get_credit(data):
    try:
        credit = data["course"]["credit"]
    except:
        credit = "null"
    return credit


def get_contact_phone(data):
    try:
        contact_phone = data["course"]["educationalRole"][0]["person"]["phone"]
    except:
        contact_phone = "null"
    return contact_phone


def get_contact_office(data):
    try:
        contact_office = data["course"]["educationalRole"][0]["person"]["officeAddress"]
    except:
        contact_office = "null"
    return contact_office


def get_contact_mail(data):
    try:
        contact_mail = data["course"]["educationalRole"][0]["person"]["email"]
    except:
        contact_mail = "null"
    return contact_mail


def get_contact_name(data):
    try:
        contact_name = data["course"]["educationalRole"][0]["person"]["displayName"]
    except:
        contact_name = "null"
    return contact_name


def get_assessment_form(data):
    assessment_form = "null"
    number = len(data["course"]["assessment"])
    liste = [" "] * number
    for i in range(0, number):
        try:
            liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
        except:
            liste[i] = "null"

        assessment_form = ' and '.join(liste)

    return assessment_form


def get_exam_date(data):
    try:
        exam_date = data["course"]["assessment"][0]["date"]
        exam_date = format_date(exam_date)
    except:
        exam_date = "null"

    return exam_date


def add_user(username: str, password: str, facebook_id: int):
    data = []
    data.append(username)
    data.append(password)
    data.append(facebook_id)

    # Adds the data to the table
    conn = database.DatabaseConnector.connection
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO `user`(`username`,`password`,`facebook_id`) VALUES (?,?,?)", data)
    except:
        cur.execute("UPDATE `user` SET password = ?, facebook_id = ? where username = \"" + username + "\"", data[1:3])
    conn.commit()





def get_term(data):
    try:
        term = data["course"]["assessment"][0]["realExecutionTerm"]
    except KeyError:
        term = "Term not available"
    return term


"""
def set_year():
    # Fetch the course
    data = get_data()
    try:
        year = int(data["course"]["assessment"][0]["realExecutionYear"])
    except KeyError:
        year = "Year not available"



def set_is_active_course():
    # todo check for this on a smart place.
    try:
        get_year()
        get_term()

        # default value for end of course
        end_of_course = None

        # checks which term the course is taught, and assigns an appropiate value to end_of_course
        if term == "Autumn":
            end_of_course = datetime(year, 12, 31)
        elif term == "Spring":
            end_of_course = datetime(year, 6, 30)

        # checks if the end_of_course is in the future, and returns the boolean
        course_active = datetime.now() < end_of_course

    except KeyError:
        course_active = "Can not check for active course"

def set_course_content():
    # Fetch the course
    data = get_data()
    x = len(data["course"]["infoType"])
    index = 0
    for i in range(0, x):
        try:
            name = data["course"]["infoType"][i]["name"]
            if (name == "Academic content"):
                index = i
        except KeyError:
            course_content = "Course content is not available"
    try:
        course_content = data["course"]["infoType"][index]["text"]
    except KeyError:
        course_content = "Course content is not available"



def is_valid_course():
    data = get_data()
    try:
        cred = data["course"]["credit"]
        return True
    except TypeError:
        return False
"""


def get_data(course_code):
    data = requests.get(base_url + course_code).json()
    return data


def get_course_name(data) -> str:
    try:
        course_name = data["course"]["englishName"]
    except:
        course_name = "null"

    return course_name


def format_date(date: str) -> str:
    year = int(float(date[0:4]))
    month = int(float(date[5:7]))
    day = int(float(date[8:]))
    date_time = datetime(year, month, day)
    date_string = "{:%B %d, %Y}".format(date_time)
    return date_string


def add_assignment_data(course_code, title, index, mandatory, published, deadline, location, category, description):
    # Adds data to a list for insertion into table
    assignment = []
    assignment.append(course_code)
    assignment.append(index)
    assignment.append(category)
    assignment.append(title)
    assignment.append(description)
    assignment.append(published)
    assignment.append(deadline)
    assignment.append(location)
    assignment.append(mandatory)

    # Adds the data to the table
    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO assignment(course_code, nr, category, title, description, published, deadline, "
                       "delivery_location, mandatory) VALUES (?,?,?,?,?,?,?,?,?)", assignment)
    except:
        cursor.execute("UPDATE assignment SET course_code = ?, nr = ?, category = ?, title = ?, description = ?, "
                       "published = ?, deadline = ?, delivery_location = ?, mandatory = ? WHERE course_code = \""
                       + course_code + "\" and category = \"" + category + "\" and nr = " + str(index), assignment)

    connection.commit()


def add_user_has_course(username, course_code):
    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()

    data_list = []
    data_list.append(username)
    data_list.append(course_code)

    try:
        cursor.execute("INSERT INTO user_has_course(username, course_code) "
                       "VALUES(?,?)", data_list)
    except:
        pass

    connection.commit()


def add_user_completed_assignment(username, course_code, nr, category, score):
    data_list = []
    data_list.append(username)
    data_list.append(course_code)
    data_list.append(nr)
    data_list.append(category)
    data_list.append(score)

    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO user_completed_assignment(username, course_code, nr, category, score)"
                       "values(?,?,?,?,?)", data_list)
    except:
        cursor.execute("UPDATE user_completed_assignment "
                       "SET score = ? " +
                       "WHERE username = \"" + username + "\" " +
                       "and  course_code = \"" + course_code + "\" " +
                       "and  nr = \"" + str(nr) + "\" " +
                       "and category =\"" + category + "\"", str(score))

    connection.commit()
