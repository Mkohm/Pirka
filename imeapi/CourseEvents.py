import requests
from datetime import datetime
import calendar
from database import DatabaseInserter


class CourseEvents:
    """
    This class aggregates all event info from the course's ntnu.no timetable, and stores it in the database.
    There is some redundancy between this class and Events(), and that should be fixed at next opportunity.
    To extract all the course events, and store it in the database, a call to get_list_of_events() is needed.
    This is not the most elegant solution, and could also be improved at the next opportunity.
    """

    def __init__(self, course_code):
        """
        Initalizes the class.
        :param course_code: The course code the method will handle
        """
        self.course_code = course_code.upper()
        self.data = self.get_data()  # stores the whole timetable for a given course
        self.number_of_weekly_events = self.get_number_of_weekly_events()  # the number of unique recurring events
        self.event_list = self.get_list_of_events() # returns a list of all events in a course, and stores it in the database

    def get_data(self):
        """
        Finds the JSON-feed for the timetable for the given course.
        :return: Returns the JSON-converted dictionary, such that it can easily be stored as a member variable.
        """
        start_of_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_" \
                       "lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=" \
                       "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode="

        end_of_url = "&year=2016&version=1"

        url = start_of_url + self.course_code + end_of_url

        try:
            data_dict = requests.get(url).json()
            return data_dict["course"]["summarized"]
        except:
            return None

    def get_number_of_weekly_events(self):
        """
        Finds the number of unique weekly events for a course.
        :return: The number of weekly events.
        """
        # no support for courses where mutiple instances for the same event is stored in JSON, i.e. courses which have
        # multiple exercise lecture at the same time, but for different groups at different places.
        return len(self.data)

    def get_list_of_events(self):
        """
        Finds all events, with relevant info, and stores it in the database
        :return: A list, of type Events(), of all the events
        """
        event_list = []

        for index in range(0, self.number_of_weekly_events):
            event_list.append(Event(index, self.course_code))

        return event_list


class Event:
    """
    A class to handle all the relevant information for one single instance of an, possible recurring, event.
    """

    def __init__(self, event_index, course_code):
        """
        Initializes the class, and stores necessary info.
        :param event_index: Used to determine which event from the timetable at the course page at ntnu.no
        :param course_code: The course code the method will handle
        """
        self.event_index = event_index  # first event in a course time table
        self.course_code = course_code.upper() # makes sure the course_code is in correct format
        self.data = self.get_data()  # converts the JSON source to a python dict
        self.day = self.get_day_index()  # stores the event day as a int from 1 to 7
        self.room = self.get_event_room()  # stores the location of the event.
        self.start_time = self.get_start_time()  # gets the starting time for the event.
        self.end_time = self.get_end_time()  # gets the end time for the event.
        self.type = self.get_event_type()  # stores the event type as an abbreviation (based on NTNU's system), FOR, ØV, etc
        self.recurrences = self.get_recurrences()  # number of recurrences
        self.week_dict = self.get_week_dict()  # dict with every lecture/guidance week as key and event info as value
        self.study_programmes = self.get_study_programmes()

        # loops through every occurrence of the event, and stores it in the database. Not the most efficient solution.
        self.get_all_events()

    def get_data(self):
        """
        Finds the JSON-feed for the timetable for the given course.
        :return: Returns the JSON-converted dictionary, such that it can easily be stored as a member variable.
        """
        start_of_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_" \
                       "lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=" \
                       "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode="

        end_of_url = "&year=2016&version=1"

        url = start_of_url + self.course_code + end_of_url
        try:
            data_dict = requests.get(url).json()
            return data_dict["course"]["summarized"][self.event_index]
        except:
            return None

    def get_day_index(self):
        """
        :return: The day index, where sunday = 0, for the event.
        """
        try:
            return self.data["dayNum"]
        except:
            pass

    def get_day(self):
        """
        :return: The name of the weekday the event occurs
        """
        try:
            day = self.data["dayNum"]
            return calendar.day_name[day - 1]
        except:
            pass

    def get_start_time(self):
        """
        :return: The starting time for the event in the format hh:mm
        """
        try:
            return self.data["from"]
        except:
            pass

    def get_end_time(self):
        """
        :return: The ending time for the event in the format hh:mm
        """
        try:
            return self.data["to"]
        except:
            pass

    def get_recurrences(self):
        """
        This method makes it easier to loop through an event, and find all instances of it.
        :return: The number of unique time intervalls for the reccuring event.
        """
        try:
            return len(self.data["weeks"])
        except:
            pass

    def get_event_type(self):
        """
        :return: The type (category) of the event
        """
        try:
            typ = self.data["acronym"]
            if typ == "FOR":
                return "Lecture"
            elif typ == "ØV":
                return "Guidance"
            else:
                return typ
        except:
            pass

    def get_event_room(self):
        """
        :return: The room where the event takes place
        """
        # When multiple rooms exsists, only the first room is taking into consideration.
        try:
            return self.data["rooms"][0]["romNavn"]
        except:
            pass

    # the week entities (the week numbers) an event occurs in is stored as a list. The elements of the list is either
    # a week interval, with a start and end week, or a single week number. The index-varible is used to loop through
    # this list.
    def get_week_entities(self, index):
        """
        the week entities (the week numbers) an event occurs in is stored as a list. The elements of the list is either
        a week interval, with a start and end week, or a single week number. The index-varible is used to loop through
        this list.
        :param index: Used to determine which row in timetable at ntnu.no the method should handle.
        :return: A list of all instances of one recurring event.
        """

        # returns the starting and ending week for an event as a list.
        # for a non-recurring event a list with two identical entities is return (the week number the event occurs in).
        try:
            week_list = self.data["weeks"][index]
        except:
            pass

        # changes week intervals from string to list for easier manipulation later. This is done by storing the
        # start and end week as a list of strings, and the convert it to a list of ints.
        week_list = week_list.split("-")

        # workaround to make sure the return value consists of two string elements
        week = ["a", "b"]

        # converts string values to int
        if len(week_list) == 2:
            week[0] = int(week_list[0])
            week[1] = int(week_list[1])
        else:
            week[0] = int(week_list[0])
            week[1] = int(week_list[0])

        return week


    def get_week_dict(self):
        """
        :return: A dictionary of every recurrence of one event.
        """

        week_dictionary = {}

        for index in range(0, self.recurrences):
            # extracts time interval in the format [start week, end week]
            week = self.get_week_entities(index)

            # adds every week entry in an interval spanning multiple week.
            for week_number in range(week[0], week[1]):
                # print(week_number)
                # print(type(week_number))
                week_dictionary[week_number] = self.event_to_string(week_number)

            # add an entry for a one-week event.
            if week[0] == week[1]:
                week_dictionary[week[0]] = self.event_to_string(week[0])

        return week_dictionary

    def event_to_string(self, week_index):
        """
        Creates a suitable formatted string of the week and info for a certain event.
        :param week_index: The index is used to find the relevant week from the week list.
        :return: A string with all the info
        """
        if week_index < 10:
            return "Week:  " + str(week_index) + " " + str(
                self.get_day()) + " " + self.start_time + "-" + self.end_time + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + " for " + self.get_study_programmes() + "\n"
        else:
            return "Week: " + str(week_index) + " " + str(
                self.get_day()) + " " + self.start_time + "-" + self.end_time + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + " for " + self.get_study_programmes() + "\n"

    @staticmethod
    def week_string_to_date(year, week, day, hour, mins):
        """
        Converts a date given by the integer parameters weekday, week and year to a datetime object given by
        day, month and year. Should probably have a different name, to better reflect it's functionality
        :param year: The year one wants to convert
        :param week: The week
        :param day: The day
        :param hour: Starting hour for the event
        :param mins: Starting minutes for the event
        :return: A datetime object given by day, month and year
        """
        date_string = str(year) + "-" + str(week) + "-" + str(day) + "-" + str(hour) + "-" + str(mins)
        return datetime.strptime(date_string, "%Y-%W-%w-%H-%M")

    def get_event(self, week_number):
        """
        Returns the event at key 'week_number' in the week_dict
        :param week_number: The key for week_dict
        :return: The event object
        """
        return self.week_dict[week_number]

    def get_all_events(self):
        """
        Iterates through all the occurences of an event, and store the relevant info the to database.
        """

        i = 0
        for index in range(0, self.recurrences):
            # extracts time interval in the format [start week, end week]
            week = self.get_week_entities(index)
            i += 1
            for week_number in range(week[0], week[1]):
                print(week_number)
                print("Event from A: " + str(i))
                print(
                    Event.week_string_to_date(2017, week_number, self.day, self.start_time[0:2], self.start_time[3:5]))
                date = str(Event.week_string_to_date(2017, week_number, self.day, self.start_time[0:2],
                                                 self.start_time[3:5]))
                DatabaseInserter.add_course_event(date, self.course_code, self.room, self.type)

            if week[0] == week[1]:
                print(week_number)
                print("Event from B: " + str(i))
                print(
                    Event.week_string_to_date(2017, week_number, self.day, self.start_time[0:2], self.start_time[3:5]))
                date = str(Event.week_string_to_date(2017, week_number, self.day, self.start_time[0:2],
                                                 self.start_time[3:5]))
                DatabaseInserter.add_course_event(date, self.course_code, self.room, self.type)

    def to_string(self):
        """
        A method to print event info in a more readable format
        """
        line = ""

        for week in self.week_dict:
            line += self.event_to_string(week)

        return line

    def get_study_programmes(self):
        """
        Finds all the study programmes involved in a given event.
        """
        program_list = self.data["studyProgramKeys"]

        programmes = program_list[0]

        for i in range(1, len(program_list)):
            programmes += ", " + program_list[i]

        return programmes
