from datetime import datetime

import requests

from database import DatabaseConnector

base_url = "http://www.ime.ntnu.no/api/course/en/"


def add_subject_data(course_code: str):
    """
    This method will get all the useful data from one course code
     - and is inserting this into the subject table in the database.
    :param course_code: The course code that all the data should be derived from
    :return: nothing
    """

    #Get data to work with
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
    course_material = get_course_material(data)
    teaching_form = get_teaching_form(data)
    prereq_knowledge = get_prereq_knowledge(data)

    # Adds the data to an list for insertion into the table
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
    data.append(course_material)
    data.append(teaching_form)

    # Adds the data to the table
    connection = DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `teaching_form`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    except:
        cursor.execute("UPDATE `course` SET course_name = ?, exam_date = ?, assessment_form = ?, contact_name = ?, contact_mail = ?, contact_office = ?, contact_phone = ?, credit = ?, url = ?, prereq_knowledge = ?, course_content = ?, teaching_form = ? WHERE course_code = \"" + course_code + "\"", data[1:13])


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


def get_teaching_form(data):
    try:
        teaching_form = data["course"]["infoType"][5]["text"]
    except:
        teaching_form = "null"

    return teaching_form


def get_course_material(data):
    try:
        course_material = data["course"]["infoType"][4]["text"]
    except:
        course_material = "null"
    return course_material


def get_url(data):
    try:
        url = data["course"]["infoType"][1]["text"]
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
    liste = [0] * number
    for i in range(0, number):
        try:
            liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
        except:
            assessment_form = "null"

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
    conn = DatabaseConnector.connection
    cur = conn.cursor()
    cur.execute("INSERT INTO `user`(`username`,`password`,`facebook_id`) VALUES (?,?,?)", data)
    conn.commit()

"""


def set_term():
    # Fetch the course
    data = get_data()
    try:
        term = data["course"]["assessment"][0]["realExecutionTerm"]
    except KeyError:
        term = "Term not available"


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


add_subject_data("TTK4105")