from unittest import TestCase

from database import DatabaseInserter
from database import DatabaseConnector

class TestDatabaseInserter(TestCase):

    #the following tests are together testing add_subject_data

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

    def test_insert_course_name(self):
        DatabaseInserter.add_subject_data("TDT4140")
        ans = DatabaseConnector.get_values("Select course_name from course where course.course_code = "
                                           "\"TDT4140\"")
        self.assertEqual("Software Engineering", ans[0][0])

        DatabaseInserter.add_subject_data("TMR4160")
        ans = DatabaseConnector.get_values("Select course_name from course where course.course_code = "
                                           "\"TMR4160\"")
        self.assertEqual("Computer Methods for the Engineer", ans[0][0])

    def test_insert_assessment_form(self):
        DatabaseInserter.add_subject_data("TDT4140")
        ans = DatabaseConnector.get_values("Select assessment_form from course where course.course_code = "
                                           "\"TDT4140\"")
        self.assertEqual("Work", ans[0][0])

        DatabaseInserter.add_subject_data("TDT4145")
        ans = DatabaseConnector.get_values("Select assessment_form from course where course.course_code = "
                                           "\"TDT4145\"")
        self.assertEqual("Written examination", ans[0][0])

    def test_insert_assessment_form_combination(self):
        DatabaseInserter.add_subject_data("TTK4135")
        ans = DatabaseConnector.get_values("Select assessment_form from course where course.course_code = "
                                           "\"TTK4135\"")
        self.assertEqual("Written examination and Work and Semester assignment", ans[0][0])

        DatabaseInserter.add_subject_data("TMR4320")
        ans = DatabaseConnector.get_values("Select assessment_form from course where course.course_code = "
                                           "\"TMR4320\"")
        self.assertEqual("Work and Written examination", ans[0][0])

    def test_insert_contact_name(self):
        DatabaseInserter.add_subject_data("TMR4105")
        ans = DatabaseConnector.get_values("Select contact_name from course where course.course_code = "
                                           "\"TMR4105\"")
        self.assertEqual("Håvard Holm", ans[0][0])

        DatabaseInserter.add_subject_data("TTK4105")
        ans = DatabaseConnector.get_values("Select contact_name from course where course.course_code = "
                                           "\"TTK4105\"")
        self.assertEqual("Trond Andresen", ans[0][0])

    def test_insert_contact_mail(self):
        DatabaseInserter.add_subject_data("TMA4115")
        ans = DatabaseConnector.get_values("Select contact_mail from course where course.course_code = "
                                           "\"TMA4115\"")
        self.assertEqual("aslak.buan@ntnu.no", ans[0][0])

        DatabaseInserter.add_subject_data("TDT4140")
        ans = DatabaseConnector.get_values("Select contact_mail from course where course.course_code = "
                                           "\"TDT4140\"")
        self.assertEqual("pekka.abrahamsson@ntnu.no", ans[0][0])

    def test_insert_contact_office_exists(self):
        DatabaseInserter.add_subject_data("TDT4145")
        ans = DatabaseConnector.get_values("Select contact_office from course where course.course_code = "
                                           "\"TDT4145\"")
        self.assertEqual("Sem Sælands vei 9, IT-bygget * 209", ans[0][0])

        DatabaseInserter.add_subject_data("TMA4105")
        ans = DatabaseConnector.get_values("Select contact_office from course where course.course_code = "
                                           "\"TMA4105\"")
        self.assertEqual("Alfred Getz vei 1, Sentralbygg II * 1248", ans[0][0])

    def test_insert_contact_office_not_exists(self):
        DatabaseInserter.add_subject_data("TTK4115")
        ans = DatabaseConnector.get_values("Select contact_office from course where course.course_code = "
                                           "\"TTK4115\"")
        self.assertEqual("null", ans[0][0])

    def test_insert_contact_phone_exists(self):
        DatabaseInserter.add_subject_data("TDT4145")
        ans = DatabaseConnector.get_values("Select contact_phone from course where course.course_code = "
                                           "\"TDT4145\"")
        self.assertEqual("73550382", ans[0][0])

        DatabaseInserter.add_subject_data("TTK4105")
        ans = DatabaseConnector.get_values("Select contact_phone from course where course.course_code = "
                                           "\"TTK4105\"")
        self.assertEqual("73594358", ans[0][0])

    def test_insert_contact_phone_not_exists(self):
        DatabaseInserter.add_subject_data("TTK4115")
        ans = DatabaseConnector.get_values("Select contact_phone from course where course.course_code = "
                                           "\"TTK4115\"")
        self.assertEqual("null", ans[0][0])

    def test_insert_credit(self):
        DatabaseInserter.add_subject_data("IØ1000")
        ans = DatabaseConnector.get_values("Select credit from course where course.course_code = "
                                           "\"IØ1000\"")
        self.assertEqual("15", ans[0][0])

        DatabaseInserter.add_subject_data("TEP4100")
        ans = DatabaseConnector.get_values("Select credit from course where course.course_code = "
                                           "\"TEP4100\"")
        self.assertEqual("7.5", ans[0][0])

    def test_insert_url_exists(self):
        DatabaseInserter.add_subject_data("TDT4105")
        ans = DatabaseConnector.get_values("Select url from course where course.course_code = "
                                           "\"TDT4105\"")
        self.assertEqual("http://itgk.idi.ntnu.no", ans[0][0])

        DatabaseInserter.add_subject_data("TMA4105")
        ans = DatabaseConnector.get_values("Select url from course where course.course_code = "
                                           "\"TMA4105\"")
        self.assertEqual("http://wiki.math.ntnu.no/tma4105", ans[0][0])

    def test_insert_url_not_exists(self):
        DatabaseInserter.add_subject_data("TTK4105")
        ans = DatabaseConnector.get_values("Select url from course where course.course_code = "
                                           "\"TTK4105\"")
        self.assertEqual("null", ans[0][0])

    def test_insert_course_material(self):
        DatabaseInserter.add_subject_data("TTK4115")
        ans = DatabaseConnector.get_values("Select course_material from course where course.course_code = "
                                           "\"TTK4115\"")
        self.assertEqual("Information will be given when the course starts.", ans[0][0])

    def test_insert_teaching_form(self):
        DatabaseInserter.add_subject_data("TMR4160")
        ans = DatabaseConnector.get_values("Select teaching_form from course where course.course_code = "
                                           "\"TMR4160\"")
        self.assertEqual("Lectures and exercises.", ans[0][0])



    def test_insert_prerequired_knowledge(self):
        DatabaseInserter.add_subject_data("TKT4116")
        ans = DatabaseConnector.get_values("Select prereq_knowledge from course where course.course_code = "
                                           "\"TKT4116\"")
        self.assertEqual("TMA4100 Calculus 1.", ans[0][0])

        DatabaseInserter.add_subject_data("TDT4145")
        ans = DatabaseConnector.get_values("Select prereq_knowledge from course where course.course_code = "
                                           "\"TDT4145\"")
        self.assertEqual("Knowledge and skills equivalent to TDT4100 Object-Oriented Programming and TDT4120 "
                         "Algorithms and Data Structures. Java is used as the programming language in "
                         "projects and exercises.", ans[0][0])

    def test_insert_term(self):
        DatabaseInserter.add_subject_data("TMA4110")
        ans = DatabaseConnector.get_values("Select term from course where course.course_code = "
                                           "\"TMA4110\"")
        self.assertEqual("Autumn", ans[0][0])

    # end of testing add_subject_data

    def test_insert_add_assignment_data(self):
        DatabaseInserter.add_assignment_data("TDT4100", "Assignment 3", 3, 1, "January 23, 2017", "February 8, 2017", "Blackboard",
                                             "exercise", "The first exercise in this course")
        ans = DatabaseConnector.get_values("Select * from assignment where assignment.course_code = \"TDT4100\"" + 
                                           "and title = \"Assignment 3\"")
        self.assertEqual("TDT4100", ans[0][0])
        self.assertEqual("Assignment 3", ans[0][3])
        self.assertEqual(3, ans[0][1])
        self.assertEqual(1, ans[0][8])
        self.assertEqual("The first exercise in this course", ans[0][4])




























