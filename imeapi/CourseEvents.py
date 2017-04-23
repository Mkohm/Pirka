import requests
# import json
from datetime import datetime
import calendar


base_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_lifecycle=" \
           "2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=cacheLevelPage&p_p_col_id=" \
           "column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode=TFY4170&_" \
           "coursedetailsportlet_WAR_courselistportlet_version=1&_coursedetailsportlet_WAR_courselistportlet_" \
           "year=2016&year=2016&version=1"


# TODO: Change implementation to use json_url in favor of base_url
start_of_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_" \
            "lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=" \
            "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode="
end_of_url = "&year=2016&version=1"

# course_code = input("Fagkode: ").upper()
# json_url = start_of_url + course_code + end_of_url

# todo: implement error checking
# todo: implement code to handle different courses, and not only FYSIKK 2

# this class aggregates all event info from all event based on the course's ntnu.no timetable.
class CourseEvents:
    # todo: implement at least the listed functions

    def __init__(self):
        self.data = self.get_data()  # stores the whole timetable for a given course
        self.number_of_weekly_events = self.get_number_of_weekly_events()  # the number of unique recurring events
        self.event_list = self.get_list_of_events()
        self.event_days = self.get_list_of_event_days()

    def get_data(self):
        data_dict = requests.get(base_url).json()
        return data_dict["course"]["summarized"]

    def get_number_of_weekly_events(self):
    # no support for courses where mutiple instances for the same event is stored in JSON, i.e. courses which have
    # multiple exercise lecture at the same time, but for different groups at different places.
        return len(self.data)

    def get_list_of_events(self):
        event_list = []

        for index in range(0, self.number_of_weekly_events):
            event_list.append(Event(index))

        return event_list

    def get_list_of_event_days(self):

        list_of_days = []

        for event in self.event_list:
            list_of_days.append(event.get_day_index())
            print(event.get_day_index())

        return list_of_days

    def get_next_event(self):

        next_event = self.event_list[0].get_next_event()
        event_info = self.event_list[0]

        for event in self.event_list:
            # event_date is a datetime object
            event_date = event.get_next_event()
            if event_date < next_event:
                next_event = event_date
                event_info = event

        week = datetime.date(next_event).isocalendar()[1]
        return event_info.get_event(week)

    def get_weekly_overview(self, week_index):

        res = ""
        # todo: remove redundant info from string, lik "Week :" on every line
        for event in self.event_list:
            res += event.event_to_string(week_index)

        return res

# this class stores all info for one, 1, event based on the official course timetable on ntnu.no.
class Event:
    # todo: implement function to differentiate different course parallels and study programmes.
    def __init__(self, event_index):
        self.event_index = event_index  # first event in a course time table -> index = 1 etc
        self.data = self.get_data()  # converts the JSON source to a python dict
        self.day = self.get_day_index()  # stores the event day as a int from 1 to 7
        self.room = self.get_event_room()  # stores the location of the event.
        self.start_time = self.get_start_time()  # gets the starting time for the event.
        self.end_time = self.get_end_time()  # gets the end time for the event.
        self.type = self.get_event_type()  # stores the event type as an abbreviation (based on NTNU's system), FOR, ØV, etc
        self.recurrences = self.get_recurrences()  # number of recurrences
        self.week_dict = self.get_week_dict()  # dict with every lecture/guidance week as key and event info as value
        self.next_event = self.get_next_event()  # TODO: move functionality to databaseExtractor after the remainding functionalty is change to take regard to database system
        self.study_programmes = self.get_study_programmes()

    def get_data(self):
        data_dict = requests.get(base_url).json()
        return data_dict["course"]["summarized"][self.event_index]

    def get_day_index(self):
        return self.data["dayNum"]

    def get_day(self):
        day = self.data["dayNum"]
        return calendar.day_name[day-1]

    def get_start_time(self):
        return self.data["from"]

    def get_end_time(self):
        return self.data["to"]

    def get_recurrences(self):
        return len(self.data["weeks"])

    def get_event_type(self):
        typ = self.data["acronym"]
        if typ == "FOR":
            return "Lecture"
        elif typ == "ØV":
            return "Guidance"
        else:
            return typ

    def get_event_room(self):
        # When multiple rooms exsists, only the first room is taking into consideration.
        return self.data["rooms"][0]["romNavn"]

    # the week entities (the week numbers) an event occurs in is stored as a list. The elements of the list is either
    # a week interval, with a start and end week, or a single week number. The index-varible is used to loop through
    # this list.
    def get_week_entities(self, index):
        # returns the starting and ending week for an event as a list.
        # for a non-recurring event a list with two identical entities is return (the week number the event occurs in).
        week_list = self.data["weeks"][index]

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

    # returns a catalog of every recurrence of one event.
    def get_week_dict(self):

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

        if week_index < 10:
            return "Week:  " + str(week_index) + " " + str(
                self.get_day()) + " " + self.start_time + "-" + self.end_time + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + " for " + self.get_study_programmes() + "\n"
        else:
            return "Week: " + str(week_index) + " " + str(
                self.get_day()) + " " + self.start_time + "-" + self.end_time + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + " for " + self.get_study_programmes() + "\n"



    # TODO: move functionality.
    # When the info extracted from ntnu.no timetable is stored in a database it will make more sense to have this some
    # other place
    def get_next_event(self):

        now = datetime.now()
        current_year = now.year

        start_hour = self.start_time[0:2]
        start_min = 15

        # loops through an ordered dictionary and gets the first event in the future
        for event_key in self.week_dict:
            event_date = Event.week_string_to_date(current_year, event_key, self.day, start_hour, start_min)
            if event_date >= now:
                return event_date

        return None

    @staticmethod
    def week_string_to_date(year, week, day, hour, mins):
        date_string = str(year) + "-" + str(week) + "-" + str(day) + "-" + str(hour)+"-"+str(mins)
        return datetime.strptime(date_string, "%Y-%W-%w-%H-%M")

    def get_event(self, week_number):
        return self.week_dict[week_number]

    def to_string(self):

        line = ""

        for week in self.week_dict:
            line += self.event_to_string(week)

        return line

    def get_study_programmes(self):
        program_list = self.data["studyProgramKeys"]

        programmes = program_list[0]

        for i in range(1, len(program_list)):
            programmes += ", " + program_list[i]

        return programmes

for index in range(0, 3):
    my_event = Event(index)
    for key in my_event.get_week_dict():
        print(my_event.get_event(key))



# print(my_event.to_string())
# print("")
# print(my_event.get_next_event())
#
#
my_course = CourseEvents()
#print(my_course.get_next_event())
print(my_course.get_weekly_overview(8))

