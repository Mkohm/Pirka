from unittest import TestCase

from database import DatabaseInserter
from database import DatabaseConnector

class TestDatabaseInserter(TestCase):

    def test_insert_exam_date_exists(self):
        DatabaseInserter.add_subject_data("TTK4105")
        ans = DatabaseConnector.get_values("Select exam_date from course where course.course_code = "
                                           "\"TTK4105\"")
        self.assertEqual("June 10, 2017", ans[0][0])

        DatabaseInserter.add_subject_data("TDT4100")
        ans = DatabaseConnector.get_values("Select exam_date from course where course.course_code = "
                                           "\"TDT4100\"")
        self.assertEqual("May 16, 2017", ans[0][0])

        DatabaseInserter.add_subject_data("TDT4145")
        ans = DatabaseConnector.get_values("Select exam_date from course where course.course_code = "
                                           "\"TDT4145\"")
        self.assertEqual("June 07, 2017", ans[0][0])

    def test_insert_exam_date_not_exist(self):
        DatabaseInserter.add_subject_data("TDT4140")
        ans = DatabaseConnector.get_values("Select exam_date from course where course.course_code = "
                                           "\"TDT4140\"")
        self.assertEqual("null", ans[0][0])

        DatabaseInserter.add_subject_data("TMR4160")
        ans = DatabaseConnector.get_values("Select exam_date from course where course.course_code = "
                                           "\"TMR4160\"")
        self.assertEqual("null", ans[0][0])














