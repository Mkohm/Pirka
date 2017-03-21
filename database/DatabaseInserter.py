import requests

from database import DatabaseConnector

base_url = "http://www.ime.ntnu.no/api/course/en/"


def add_subject_data(course_code: str):
    # Fetch the course
    data = get_data(course_code)
    course_name = get_course_name(course_code)

    exam_date_string = None
    course_name = None
    assessment_form = None


    try:
        exam_date = data["course"]["assessment"][0]["date"]
        exam_date_string = format_date(exam_date)
        # exam_date = "Exam date for " + str(course_code) + " " + str(course_name) + " is " + str(exam_date_string)
    except KeyError:
        exam_date_string = None

    # Fetch the course
    number = len(data["course"]["assessment"])
    liste = [0] * number
    for i in range(0, number):
        try:
            liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
        except KeyError:
            assessment_form = None

        assessment_form = ' and '.join(liste[i])

    # Fetch the course
    try:
        course_name = data["course"]["englishName"]
    except KeyError:
        course_name = "Course name is not available"

    DatabaseConnector.add_values("INSERT INTO `subject`(`course_code`,`name`,`exam_date`, `assessment_form`) VALUES ('hest', 'hest','hest', 'hest');")


"""
def get_exam_date() -> str:
    set_exam_date()
    return exam_date


def set_assessment_form():
    # todo loop through every element in assessment

    # Fetch the course
    data = get_data()
    number = len(data["course"]["assessment"])
    liste = [0] * number
    for i in range(0, number):
        try:
            liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
        except KeyError:
            assessment_form = "No assessment form available"

    assessment_form = ' and '.join(liste)


def get_assessment_form():
    set_assessment_form()
    return assessment_form


def set_term():
    # Fetch the course
    data = get_data()
    try:
        term = data["course"]["assessment"][0]["realExecutionTerm"]
    except KeyError:
        term = "Term not available"


def get_term():
    set_term()
    return term


def set_year():
    # Fetch the course
    data = get_data()
    try:
        year = int(data["course"]["assessment"][0]["realExecutionYear"])
    except KeyError:
        year = "Year not available"


def get_year():
    set_year()
    return year


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


def get_is_active_course():
    set_is_active_course()
    return course_active


def set_contact_name():
    # Fetch the course
    data = get_data()

    try:
        contact_name = data["course"]["educationalRole"][0]["person"]["displayName"]
    except KeyError:
        contact_name = "No contact person available"


def get_contact_name() -> str:
    set_contact_name()
    return contact_name


def set_contact_mail():
    # Fetch the course
    data = get_data()
    try:
        contact_mail = data["course"]["educationalRole"][0]["person"]["email"]
    except KeyError:
        contact_mail = "Contact mail is not available"


def get_contact_mail() -> str:
    set_contact_mail()
    return contact_mail


def set_contact_office():
    # Fetch the course
    data = get_data()
    try:
        contact_office = data["course"]["educationalRole"][0]["person"]["officeAddress"]
    except KeyError:
        contact_office = "Office address is not available"


def get_contact_office() -> str:
    set_contact_office()
    return contact_office


def set_contact_phone():
    # Fetch the course
    data = get_data()
    try:
        contact_phone = data["course"]["educationalRole"][0]["person"]["phone"]
    except KeyError:
        contact_phone = "Contact phone is not available"


def get_contact_phone() -> str:
    set_contact_phone()
    return contact_phone


def set_contact_website():
    # gets the contacts person website
    mail = get_contact_mail()
    website_id = mail.split("@")

    contact_website = "https://www.ntnu.no/ansatte/" + website_id[0]


def get_contact_website() -> str:
    set_contact_website()
    return contact_website




def get_course_name(course_code) -> str:
    # Fetch the course
    data = get_data(course_code)
    try:
        course_name = data["course"]["englishName"]
    except KeyError:
        course_name = None


def set_credit():
    # Fetch the course
    data = get_data()
    try:
        credit = data["course"]["credit"]
    except KeyError:
        credit = "Course credit not available"


def get_credit():
    set_credit()
    return credit


def set_url():
    # Fetch the course
    data = get_data()
    try:
        url = data["course"]["infoType"][1]["text"]
    except KeyError:
        url = "Course url not available"


def get_url() -> str:
    set_url()
    return url


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


def get_course_material() -> str:
    set_course_material()
    return course_material


def set_teaching_form():
    # Fetch the course
    data = get_data()
    try:
        teaching_form = data["course"]["infoType"][5]["text"]
    except KeyError:
        teaching_form = "Teaching form is not available for this course"


def get_teaching_form() -> str:
    set_teaching_form()
    return teaching_form


def set_events():
    pass


def get_events():
    set_events()
    return events


def get_data(course_code):
    data = requests.get(base_url + course_code).json()
    return data


def is_valid_course():
    data = get_data()
    try:
        cred = data["course"]["credit"]
        return True
    except TypeError:
        return False
"""

def format_date(date: str) -> str:
    year = int(float(date[0:4]))
    month = int(float(date[5:7]))
    day = int(float(date[8:]))
    date_time = datetime(year, month, day)
    date_string = "{:%B %d, %Y}".format(date_time)
    return date_string
