from datetime import datetime
import time

import database.DatabaseConnector
import imeapi.ImeApiDataReceiver as ime


def add_user(username: str, password: str, facebook_id: int):
    """
    Inserts a user to the database
    :param username: users username
    :param password: users password
    :param facebook_id: users unique facebook id
    :return: nothing
    """

    data = []
    data.append(username)
    data.append(password)
    data.append(facebook_id)
    data.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))

    # Adds the data to the table
    conn = database.DatabaseConnector.connection
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO `user`(`username`,`password`,`facebook_id`,`registry_date`) VALUES (?,?,?,?)", data)
    except:
        cur.execute("UPDATE `user` SET password = ?, facebook_id = ? where username = \"" + username + "\"", data[1:3])
    conn.commit()

def add_assignment_data(course_code, title, index, mandatory, published, deadline, location, category, description):
    """
    Adds a new assignment to the database
    :param course_code: the courses course code
    :param title: the assignment title
    :param index: the number of the assignment
    :param mandatory: if the assignment is mandatory
    :param published: when the assignment was published
    :param deadline: when the assignment should be delivered
    :param location: where the assignment should be delivered
    :param category: what type of assignment it is
    :param description: description of the assignment
    :return: nothing
    """

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
        cursor.execute("INSERT INTO `assignment`(`course_code`, `nr`, `category`, `title`, `description`, `published`, `deadline`, "
                       "`delivery_location`, `mandatory`) VALUES (?,?,?,?,?,?,?,?,?)", assignment)
    except:
        cursor.execute("UPDATE assignment SET course_code = ?, nr = ?, category = ?, title = ?, description = ?, "
                       "published = ?, deadline = ?, delivery_location = ?, mandatory = ? WHERE course_code = \""
                       + course_code + "\" and category = \"" + category + "\" and nr = " + str(index), assignment)

    connection.commit()

def add_user_has_course(username, course_code):
    """
    Adds to the database that a user has a course
    :param username: users username
    :param course_code: courses course code
    :return: 
    """


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

def add_itslearning_url(url: str):
    """
    Adds a itslearning ical url to the database
    :param url: the ical url
    :return: nothing
    """

    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()

    data_list = []
    data_list.append(url)

    try:
        cursor.execute("INSERT INTO `user`(`ical_itslearning`) "
                       "VALUES(?)", data_list)
    except:
        pass

    connection.commit()

def add_user_completed_assignment(username, course_code, nr, category, score):
    """
    Adds to the database that a user have completed an assignment
    :param username: users username
    :param course_code: course course code
    :param nr: the number of the assignment
    :param category: the assignment category 
    :param score: score is 1 if it was completed, 0 else
    :return: nothing
    """

    #create variable for all fields to be added to database
    data_list = []
    data_list.append(username)
    data_list.append(course_code)
    data_list.append(nr)
    data_list.append(category)
    data_list.append(score)

    #establish connection to database
    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO `user_completed_assignment`(`username`, `course_code`, `nr`, `category`, `score`)"
                       "values(?,?,?,?,?)", data_list)
    except:
        cursor.execute("UPDATE user_completed_assignment "
                       "SET score = ? " +
                       "WHERE username = \"" + username + "\" " +
                       "and  course_code = \"" + course_code + "\" " +
                       "and  nr = \"" + str(nr) + "\" " +
                       "and category =\"" + category + "\"", str(score))

    connection.commit()

def add_course_event(date_time, course_code, room, category):
    """
    Adds an event to a course in the database
    :param date_time: when the event is
    :param course_code: the course code
    :param room: where the event is
    :param category: what kind of event this is
    :return: nothing
    """

    #create variable for all fields to be added to database
    data_list=[]
    data_list.append(date_time)
    data_list.append(course_code)
    data_list.append(room)
    data_list.append(category)

    #establish connection to database
    connection = database.DatabaseConnector.connection
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO `course_event`(`date_time`, `course_code`, `room`, `category`) VALUES(?,?,?,?)", data_list)
    except:
        pass

    connection.commit()

def add_subject_data(course_code: str):
    """
    This method will get all the useful data from one course code
     - and is inserting this into the subject table in the database.
    :param course_code: The course code that all the data should be derived from
    :return: nothing
    """

    # Get data to work with
    data = ime.get_data(course_code)

    course_name = ime.get_course_name(data)
    exam_date = ime.get_exam_date(data)

    if exam_date != "null":
        time1 = time.strptime(exam_date, '%B %d, %Y')
        exam_date = time.strftime('%Y-%m-%d', time1)

    assessment_form = ime.get_assessment_form(data)
    contact_name = ime.get_contact_name(data)
    contact_mail = ime.get_contact_mail(data)
    contact_office = ime.get_contact_office(data)
    contact_phone = ime.get_contact_phone(data)
    credit = ime.get_credit(data)
    url = ime.get_url(data)
    course_content = ime.get_course_content(data)
    course_material = ime.get_course_material(data)
    teaching_form = ime.get_teaching_form(data)
    prereq_knowledge = ime.get_prereq_knowledge(data)
    term = ime.get_term(data)

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


def format_date(date: str) -> str:
    """
    Formats the date to a more user friendly format
    :param date: a string containing a date
    :return: a user friendly string representing a date
    """

    year = int(float(date[0:4]))
    month = int(float(date[5:7]))
    day = int(float(date[8:]))
    date_time = datetime(year, month, day)
    date_string = "{:%B %d, %Y}".format(date_time)
    return date_string
