import requests
# import json
from datetime import datetime
import calendar


base_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_lifecycle=" \
           "2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=cacheLevelPage&p_p_col_id=" \
           "column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode=TFY4170&_" \
           "coursedetailsportlet_WAR_courselistportlet_version=1&_coursedetailsportlet_WAR_courselistportlet_" \
           "year=2016&year=2016&version=1"

# todo: implement error checking
# todo: add return type?
# todo: implement code to handle different courses, and not only FYSIKK 2


class CourseEvents:
    # todo: implement at least the listed functions

    def __init__(self):
        self.data = self.get_data()  # stores whole timetable for a given course
        self.number_of_weekly_events = self.get_number_of_weekly_events()  # the number of unique recurring events
        self.event_list = self.get_list_of_events()
        self.event_days = self.get_list_of_event_days()

    def get_data(self):
        data_dict = requests.get(base_url).json()
        return data_dict["course"]["summarized"]

    def get_number_of_weekly_events(self):
        return len(self.data)

    def get_list_of_events(self):

        event_list = []

        for event_index in range(0, self.number_of_weekly_events):
            event_list.append(Event(event_index))

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


class Event:
    # todo: implement function to differentiate different course parallels and study programmes.
    def __init__(self, event_index):
        self.event_index = event_index  # first event in a course time table -> index = 1 etc
        self.data = self.get_data()  # converts the JSON source to a python dict
        self.day = self.get_day_index()  # stores the event day as a int from 1 to 7
        self.room = self.get_event_room()
        self.time_slot = self.get_time_slot()
        self.start_time = self.get_start_time()
        self.end_time = self.get_end_time()
        self.type = self.get_event_type()  # stores the event type as an abbreviation, FOR, ØV, etc
        self.number_of_events = self.get_number_of_events()  # number of recurring weeks for this event
        self.week_dict = self.get_week_dict() # dict with every lecture/guidance week as key and event info as value
        self.next_event = self.get_next_event()

    def get_data(self):
        data_dict = requests.get(base_url).json()
        return data_dict["course"]["summarized"][self.event_index]

    def get_day_index(self):
        return self.data["dayNum"]

    def get_day(self):

        day = self.data["dayNum"]

        return calendar.day_name[day-1]

    #TODO: delete code when all references to this block is removed
    def get_time_slot(self):

        start_time = self.data["from"]
        end_time = self.data["to"]
        return start_time, end_time


    def get_start_time(self):
        return self.data["from"]

    def get_end_time(self):
        return self.data["to"]

    def get_event_type(self):

        typ = self.data["acronym"]

        if typ == "FOR":
            return "Lecture"
        elif typ == "ØV":
            return "Guidance"
        else:
            return typ

    def get_event_room(self):
        # todo: fix case where there exsits multiple rooms for an event.
        return self.data["rooms"][0]["romNavn"]

    def get_week_entities(self, week_index):
        # returns the starting and ending week for an event as a list.
        # for a single week event a list with to identical entities is return.
        week_list = self.data["weeks"][week_index]

        # changes week from string to list for easier manipulation later
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

        week_dictionary = {}

        for week_index in range(0, self.number_of_events):
            # extracts time interval in the format [start week, end week]
            week = self.get_week_entities(week_index)

            # adds every week entry in an interval spanning multiple week.
            for week_number in range(week[0], week[1]):
                # print(week_number)
                # print(type(week_number))
                week_dictionary[week_number] = self.event_to_string(week_number)

            # add an entry for a one-week event.
            if week[0] == week[1]:
                week_dictionary[week[0]] = self.event_to_string(week[0])

        return week_dictionary

    def get_number_of_events(self):
        return len(self.data["weeks"])

    def event_to_string(self, week_index):
        # todo: needs better formatting?

        time_slot = self.get_time_slot()

        if week_index < 10:
            return "Week:  " + str(week_index) + " " + str(
                self.get_day()) + " " + time_slot[0] + "-" + time_slot[1] + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + "\n"
        else:
            return "Week: " + str(week_index) + " " + str(
                self.get_day()) + " " + time_slot[0] + "-" + time_slot[1] + " - " + self.get_event_type() + \
                   " in " + self.get_event_room() + "\n"

    def get_next_event(self):

        now = datetime.now()
        current_year = now.year

        start_hour = self.time_slot[0][0:2]
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


my_event = Event(0)

for key in my_event.get_week_dict():
    temp = my_event.get_event(key)


# print(my_event.to_string())
# print("")
# print(my_event.get_next_event())
#
#
#my_course = CourseEvents()
#print(my_course.get_next_event())
#print(my_course.get_weekly_overview(8))

