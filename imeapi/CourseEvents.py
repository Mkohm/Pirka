import requests
# import json
from datetime import datetime

base_url = "https://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode=TFY4170&_coursedetailsportlet_WAR_courselistportlet_version=1&_coursedetailsportlet_WAR_courselistportlet_year=2016&year=2016&version=1"

# todo: implement error checking
# todo: make enumeration class for days?
# todo: add return type?
# todo: implement code to handle different courses, and not only FYSIKK 2

class CourseEvents:
    # todo: implement at least the listed functions
    # todo: fix AttributeError for line 18-19

    def __init__(self):
        self.number_of_events = CourseEvents.get_number_of_weekly_events()
        self.event_list = self.get_list_of_events()
        self.event_days = self.get_list_of_event_days()

    def get_list_of_events(self):

        event_list = []

        for event_index in range(0, self.number_of_events):
            self.event_list.append(Event(event_index))

        return event_list

    def get_list_of_event_days(self):

        list_of_days = []

        for i in range(0, self.number_of_events):
            list_of_days[i] = self.get_list_of_events[i].get_day()
            print(list_of_days[i])

        return list_of_days

    @staticmethod
    def get_number_of_weekly_events():
        data = Event.get_data()
        return len(data["course"]["summarized"])

    def get_next_event(self):
        pass

    def get_weekly_overview(self):
        pass


class Event:
    # todo: implement function to differentiate different course parallels and study programmes.
    def __init__(self, event_index):
        self.data = self.get_data()
        self.event_index = event_index
        self.day = self.get_day()
        self.room = self.get_event_room()
        self.time_slot = self.get_time_slot()
        self.type = self.get_event_type()
        self.events = self.get_events()
        self.number_of_events = self.get_number_of_events()
        self.next_event = self.get_next_event()

    @staticmethod
    def get_data():
        return requests.get(base_url).json()

    def get_day(self):
        return self.data["course"]["summarized"][self.event_index]["dayNum"]

    def get_time_slot(self):

        start_time = self.data["course"]["summarized"][self.event_index]["from"]
        end_time = self.data["course"]["summarized"][self.event_index]["to"]
        return start_time, end_time

    def get_event_type(self):
        return self.data["course"]["summarized"][self.event_index]["acronym"]

    def get_event_room(self):
        # todo: fix case where there exsits multiple rooms for an event.
        return self.data["course"]["summarized"][self.event_index]["rooms"][0]["romNavn"]

    def get_week_entities(self, week_index):
        # returns the starting and ending week for an event as a list.
        # for a single week event a list with to identical entities is return.
        week_list = self.data["course"]["summarized"][self.event_index]["weeks"][week_index]

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

    def get_events(self):

        number_of_weeks = len(self.data["course"]["summarized"][self.event_index]["weeks"])
        week_dict = {}

        for week_index in range(0, number_of_weeks):
            # extracts time interval in the format [start week, end week]
            week = self.get_week_entities(week_index)

            # adds every week entry in an interval spanning multiple week.
            for week_number in range(week[0], week[1]):
                # print(week_number)
                # print(type(week_number))
                week_dict[week_number] = self.event_to_string(week_number)

            # add an entry for a one-week event.
            if week[0] == week[1]:
                week_dict[week[0]] = self.event_to_string(week[0])

        return week_dict

    def get_number_of_events(self):
        return len(self.events)

    def event_to_string(self, week_index):
        # todo: needs better formatting and inclusion of time_slot
        return "Week: " + str(week_index) + " " + str(
            self.get_day()) + " - " + self.get_event_type() + " i " + self.get_event_room()

    def get_next_event(self):

        now = datetime.now()
        current_day = now.weekday()
        current_week = datetime.date(now).isocalendar()[1]

        # sets a default value. Not sure is necessary
        week = 1

        # todo: make more robust
        if current_day > self.day:
            week = current_week + 1
            # todo: wont work if vacation occurs. code will try to use a non-exsisting key to index a value in the dict
        else:
            week = current_week

        return week, self.day, self.time_slot

    # todo: does not work. Wrong indexing in dict
    def get_event(self, week_number):
        return self.events[week_number]

    def to_string(self):

        # todo: return string in stead of printing
        for week in self.events:
            print(self.events[week])

        pass


my_event = Event(0)
my_event.to_string()
print("")
print(my_event.get_next_event())

my_course = CourseEvents()

CourseEvents.get_list_of_event_days()
