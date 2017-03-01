from unittest import TestCase
from imeapi.DataReceiver import DataReceiver

class TestDataReceiver(TestCase):

    def test_get_exam_date_ok_input(self):
        self.assertEqual(DataReceiver.get_exam_date("TDT4100"), "Exam date for TDT4100 Object-Oriented Programming is May 16, 2017")
        self.assertEqual(DataReceiver.get_exam_date("TMA4140"), "Exam date for TMA4140 Discrete Mathematics is December 15, 2016")
        self.assertEqual(DataReceiver.get_exam_date("TFE4120"), "Exam date for TFE4120 Electromagnetics is May 29, 2017")
        self.assertEqual(DataReceiver.get_exam_date("TTK4135"), "Exam date for TTK4135 Optimization and Control is May 20, 2017")


    def test_get_exam_date_no_exam(self):
        self.assertEqual(DataReceiver.get_exam_date("TDT4140"), "No exam date available because assessment form is: Work")
        self.assertEqual(DataReceiver.get_exam_date("TMR4160"), "No exam date available because assessment form is: Work")

    def test_get_exam_date_wrong_input(self):
        self.assertEqual(DataReceiver.get_exam_date("TMR1111"), "You entered an invalid course code.")
        self.assertEqual(DataReceiver.get_exam_date("jflsh"), "You entered an invalid course code.")

    def test_get_exam_date_course_not_active(self):
        self.assertEqual(DataReceiver.get_exam_date("TMA4100"), "No exam date available because the course is not active")



    def test_getContactInfo(self):
        self.fail()

    def test_get_course_name(self):
        self.assertEqual(DataReceiver.get_course_name("TDT4145"), "Software Engineering ellernoe")
        self.assertEqual(DataReceiver.get_course_name("TMA4100"), "Calculus 1 ufidjsg")
        self.assertEqual(DataReceiver.get_course_name("TTK4105"), "Control Systems")
        self.assertEqual(DataReceiver.get_course_name("TKT4124"), "Mechanics 3")
        self.assertEqual(DataReceiver.get_course_name("fgyjhkdlsø"),"Invalid course")
        self.assertEqual(DataReceiver.get_course_name("TMR1111"), "Invalid course")



    def test_getCredit(self):
        self.assertEqual(DataReceiver.get_credit("TMA4100"), "7.5")
        self.assertEqual(DataReceiver.get_credit("TMA4160"), "7.5")
        self.assertEqual(DataReceiver.get_credit("IØ1000"), "15.0")
        self.assertEqual(DataReceiver.get_credit("TMA4130"), "7.5")
        self.assertEqual(DataReceiver.get_credit("TEP4100"), "7.5")

    def test_get_url(self):
        self.assertEqual(DataReceiver.get_url("TMA4120"), "http://wiki.math.ntnu.no/tma4105")


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
