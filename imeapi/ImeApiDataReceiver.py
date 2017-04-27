import requests
base_url = "http://www.ime.ntnu.no/api/course/en/"



def get_prereq_knowledge(data):
    """
    Extracts prerequisite knowldegde from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing prerequisite knowldege
    """

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
    """
    Extracts course content from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing course content
    """

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
    """
    Extracts teaching form from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing teaching form
    """

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
    """
    Extracts course material from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing prerequisite knowldege
    """

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
    """
    Extracts course url from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing course url
    """

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
    """
    Extracts course credit from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing course credit
    """
    try:
        credit = data["course"]["credit"]
    except:
        credit = "null"
    return credit

def get_contact_phone(data):
    """
    Extracts contact phone number from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing contact phone number
    """

    try:
        contact_phone = data["course"]["educationalRole"][0]["person"]["phone"]
    except:
        contact_phone = "null"
    return contact_phone

def get_contact_office(data):
    """
    Extracts contact office from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing contact office
    """

    try:
        contact_office = data["course"]["educationalRole"][0]["person"]["officeAddress"]
    except:
        contact_office = "null"
    return contact_office

def get_contact_mail(data):
    """
    Extracts contact mail from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing contact mail
    """

    try:
        contact_mail = data["course"]["educationalRole"][0]["person"]["email"]
    except:
        contact_mail = "null"
    return contact_mail

def get_contact_name(data):
    """
    Extracts contact name from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing contact name
    """

    try:
        contact_name = data["course"]["educationalRole"][0]["person"]["displayName"]
    except:
        contact_name = "null"
    return contact_name

def get_assessment_form(data):
    """
    Extracts assessment form from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing assessment form
    """

    assessment_form = "null"

    try:
        number = len(data["course"]["assessment"])
        liste = [" "] * number
        for i in range(0, number):
            try:
                liste[i] = data["course"]["assessment"][i]["assessmentFormDescription"]
            except:
                liste[i] = "null"

            assessment_form = ' and '.join(liste)

        return assessment_form
    except:
        assessment_form = "null"
        return assessment_form

def get_exam_date(data):
    """
    Extracts exam date from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing exam date
    """

    try:
        exam_date = data["course"]["assessment"][0]["date"]
        exam_date = format_date(exam_date)
    except:
        exam_date = "null"

    return exam_date

def get_term(data):
    """
    Extracts course term from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing course term
    """

    try:
        term = data["course"]["assessment"][0]["realExecutionTerm"]
    except:
        term = "Term not available"
    return term

def get_data(course_code):
    """
    Gets the data that we obtain all the data from using the API-url
    :param course_code: the course we want to get data from
    :return: json data that contains all the data from a course
    """

    data = requests.get(base_url + course_code).json()
    return data

def get_course_name(data) -> str:
    """
    Extracts course name from the data
    :param data: the json received from IME-API that the data should be extracted from
    :return: String containing course name
     """
    try:
        course_name = data["course"]["englishName"]
    except:
        course_name = "null"

    return course_name

