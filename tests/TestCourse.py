from unittest import TestCase
from imeapi.Course import Course

class TestCourse(TestCase):

    def test_get_exam_date_ok_input(self):
        self.assertEqual(Course("TDT4100").get_exam_date(), "Exam date for TDT4100 Object-Oriented Programming is May 16, 2017")
        self.assertEqual(Course("TMA4140").get_exam_date(), "Exam date for TMA4140 Discrete Mathematics is December 15, 2016")
        self.assertEqual(Course("TFE4120").get_exam_date(), "Exam date for TFE4120 Electromagnetics is May 29, 2017")
        self.assertEqual(Course("TTK4135").get_exam_date(), "Exam date for TTK4135 Optimization and Control is May 20, 2017")


    def test_get_exam_date_no_exam(self):
        self.assertEqual("No exam date available because assessment form is: Work", Course("TDT4140").get_exam_date())
        self.assertEqual("No exam date available because assessment form is: Work", Course("TMR4160").get_exam_date())

    def test_get_exam_date_wrong_input(self):
        self.assertEqual(Course("TMR1111").get_exam_date(), "You entered an invalid course code.")
        self.assertEqual(Course("jflsh").get_exam_date(), "You entered an invalid course code.")

    def test_get_exam_date_course_not_active(self):
        self.assertEqual(Course("TMA4100").get_exam_date(), "No exam date available because the course is not active.")



    def test_getContactInfo(self):
        self.fail()

    def test_get_course_name(self):
        self.assertEqual(Course.get_course_name("TDT4145"), "Software Engineering ellernoe")
        self.assertEqual(Course.get_course_name("TMA4100"), "Calculus 1 ufidjsg")
        self.assertEqual(Course.get_course_name("TTK4105"), "Control Systems")
        self.assertEqual(Course.get_course_name("TKT4124"), "Mechanics 3")
        self.assertEqual(Course.get_course_name("fgyjhkdlsø"), "Invalid course")
        self.assertEqual(Course.get_course_name("TMR1111"), "Invalid course")



    def test_getCredit(self):
        self.assertEqual(Course.get_credit("TMA4100"), "7.5")
        self.assertEqual(Course.get_credit("TMA4160"), "7.5")
        self.assertEqual(Course.get_credit("IØ1000"), "15.0")
        self.assertEqual(Course.get_credit("TMA4130"), "7.5")
        self.assertEqual(Course.get_credit("TEP4100"), "7.5")

    def test_get_url(self):
        self.assertEqual(Course.get_url("TMA4120"), "http://wiki.math.ntnu.no/tma4105")


    def test_getFORK(self):
        self.fail()

    def test_getContent(self):
        self.fail()

    def test_getCourseMaterial(self):
        self.fail()

    def test_getForm(self):
        self.fail()

    def test_getANBFORK(self):
        self.fail()
