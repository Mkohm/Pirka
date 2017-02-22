from unittest import TestCase


class TestDataReceiver(TestCase):

    def test_get_exam_date(self):
        self.assertEqual(get_exam_date(TDT4100), "Exam date for TDT4100 Object-Oriented Programming is 2017-05-16")
        self.assertEqual(get_exam_date(TMA4140), "Exam date for TMA4140 Discrete Mathematics is 2016-12-15")
        self.assertEqual(get_exam_date(TFE4120), "Exam date for TFE4120 Electromagnetics is 2017-05-29")
        self.assertEqual(get_exam_date(TDT4140), "No Exam date available")
        self.assertEqual(get_exam_date(TMR4160), "No Exam date available")
        self.assertEqual(get_exam_date(TTK4135), "Exam date for TTK4135 Optimization and Control is 2017-05-20")


    def test_getContactInfo(self):
        self.fail()

    def test_getCourseName(self):
        self.assertEqual()

    def test_getCredit(self):
        self.fail()

    def test_getURL(self):
        self.fail()

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
