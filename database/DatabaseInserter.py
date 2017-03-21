from datetime import datetime

import requests

from database import DatabaseConnector

base_url = "http://www.ime.ntnu.no/api/course/en/"


def add_subject_data(course_code: str):
    data = get_data(course_code)
    assessment_form = "null"

    # Fetch the course name
    try:
        course_name = data["course"]["englishName"]
    except:
        course_name = "Course name is not available"


    # Try to get the exam date
    try:
        exam_date = data["course"]["assessment"][0]["date"]
        exam_date = format_date(exam_date)
    except:
        exam_date = "null"


    # Try to get the assesment form
    try:
        number = len(data["course"]["assessment"])
        liste = [0] * number
        for i in range(0, number):
            try:
                liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
            except:
                assessment_form = "null"

            assessment_form = ' and '.join(liste)
    except:
        course_name = "null"



    # Try to get the contact name
    try:
        contact_name = data["course"]["educationalRole"][0]["person"]["displayName"]
    except:
        contact_name = "null"

    try:
        contact_mail = data["course"]["educationalRole"][0]["person"]["email"]
    except KeyError:
        contact_mail = "null"

    try:
        contact_office = data["course"]["educationalRole"][0]["person"]["officeAddress"]
    except KeyError:
        contact_office = "null"

    try:
        contact_phone = data["course"]["educationalRole"][0]["person"]["phone"]
    except KeyError:
        contact_phone = "null"

    try:
        credit = data["course"]["credit"]
    except KeyError:
        credit = "null"

    try:
        url = data["course"]["infoType"][1]["text"]
    except KeyError:
        url = "null"

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

    # Adds the data to the table
    conn = DatabaseConnector.connection
    cur = conn.cursor()
    cur.execute("INSERT INTO `subject`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`contact_website`,`url`) VALUES (?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()


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





def set_prereq_knowledge():
    # Fetch the course
    data = get_data()
    value = ""

    for i in range(0, 6):
        try:
            value = data["course"]["infoType"][i]["code"]
            if (value == "ANBFORK"):
                index = i
        except KeyError:
            prereq_knowledge = "Prerequisite knowledge is not available for this course"
    try:
        prereq_knowledge = data["course"]["infoType"][index]["text"]
    except KeyError:
        prereq_knowledge = "Prerequisite knowledge is not available for this course"


def get_prereq_knowledge() -> str:
    set_prereq_knowledge()
    return prereq_knowledge


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


def get_course_content() -> str:
    set_course_content()
    return course_content


def set_course_material():
    # Fetch the course
    data = get_data()
    try:
        course_material = data["course"]["infoType"][4]["text"]
    except KeyError:
        course_material = "Course material is not available"


def set_teaching_form():
    # Fetch the course
    data = get_data()
    try:
        teaching_form = data["course"]["infoType"][5]["text"]
    except KeyError:
        teaching_form = "Teaching form is not available for this course"




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


def get_course_name(course_code) -> str:
    # Fetch the course
    data = get_data(course_code)
    try:
        course_name = data["course"]["englishName"]
    except TypeError:
        course_name = None

    return course_name

def format_date(date: str) -> str:
    year = int(float(date[0:4]))
    month = int(float(date[5:7]))
    day = int(float(date[8:]))
    date_time = datetime(year, month, day)
    date_string = "{:%B %d, %Y}".format(date_time)
    return date_string


add_subject_data("tdt4100")