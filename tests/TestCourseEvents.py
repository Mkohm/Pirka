from unittest import TestCase

from imeapi.CourseEvents import CourseEvents, Event


class TestCourseEvents(TestCase):

    def setUp(self):
        self.event = Event(0, "TFY4170")
        self.course_event = CourseEvents("TFY4170")

    def test_get_event_day(self):
        day = self.event.get_day()
        self.assertEqual("Monday", day)

    def test_get_event_index(self):
        index = self.event.get_day_index()
        self.assertEqual(1, index)

    def test_get_event_room(self):
        room = self.event.get_event_room()
        self.assertEqual("R3", room)

    def test_get_start_time(self):
        start_time = self.event.get_start_time()
        self.assertEqual("08:15", start_time)

    def test_get_end_time(self):
        end_time = self.event.get_end_time()
        self.assertEqual("10:00", end_time)

    def test_get_event_type(self):
        typ = self.event.get_event_type()
        self.assertEqual("Lecture", typ)

    def test_get_recurrences(self):
        recurrence = self.event.get_recurrences()
        self.assertEqual(2, recurrence)

    def test_get_study_program(self):
        program = self.event.get_study_programmes()
        self.assertEqual("MIMT, MSMT, MTKJ, MTMT, MTNANO", program)

    def test_number_of_weekly_events(self):
        number = self.course_event.get_number_of_weekly_events()
        self.assertEqual(3, number)
