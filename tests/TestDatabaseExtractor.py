from unittest import TestCase

from database import DatabaseExtractor

class TestCourse(TestCase):

    #OK
    def test_get_exam_date_ok_input(self):
        self.assertEqual("Exam date in TDT4100 Object-Oriented Programming is May 16, 2017", DatabaseExtractor.get_exam_date("TDT4100"))
        self.assertEqual("Exam date in TFE4120 Electromagnetics is May 29, 2017", DatabaseExtractor.get_exam_date("TFE4120"))
        self.assertEqual("Exam date in TTK4135 Optimization and Control is May 20, 2017", DatabaseExtractor.get_exam_date("TTK4135"))

    def test_get_exam_date_no_exam(self):
        self.assertEqual("No exam date available because assessment form is: Work", DatabaseExtractor.get_exam_date("TDT4140"))
        self.assertEqual("No exam date available because assessment form is: Work", DatabaseExtractor.get_exam_date("TMR4160"))

    def test_get_exam_date_wrong_input(self):
        self.assertEqual("You entered an invalid course code.", DatabaseExtractor.get_exam_date("TMR1111"))
        self.assertEqual("You entered an invalid course code.", DatabaseExtractor.get_exam_date("jflsh"))

    def test_get_exam_date_course_not_active(self):
        self.assertEqual("No exam date available because the course is not active.", DatabaseExtractor.get_exam_date("TMA4100"))
        self.assertEqual("No exam date available because the course is not active.", DatabaseExtractor.get_exam_date("TMA4140"))

    #OK
    def test_assessment_form_written(self):
        self.assertEqual("Assessment form in TDT4100 Object-Oriented Programming is Written examination", DatabaseExtractor.get_assessment_form("TDT4100"))
        self.assertEqual("Assessment form in TDT4105 Information Technology, Introduction is Written examination", DatabaseExtractor.get_assessment_form("TDT4105"))

    #OK
    def test_assessment_form_work(self):
        self.assertEqual("Assessment form in TDT4140 Software Engineering is Work", DatabaseExtractor.get_assessment_form("TDT4140"))
        self.assertEqual("Assessment form in TMR4160 Computer Methods for the Engineer is Work", DatabaseExtractor.get_assessment_form("TMR4160"))

    #OK
    def test_assessment_form_combination(self):
        self.assertEqual("Assessment form in TTK4135 Optimization and Control is Written examination and Work and Semester assignment", DatabaseExtractor.get_assessment_form("TTK4135"))
        self.assertEqual("Assessment form in TMR4105 Marine Technology - Elementary Course is Work and Oral examination", DatabaseExtractor.get_assessment_form("TMR4105"))
        self.assertEqual("Assessment form in TMR4230 Oceanography is Oral examination and Semester assignment", DatabaseExtractor.get_assessment_form("TMR4230"))
        self.assertEqual("Assessment form in TMA4140 Discrete Mathematics is Written examination and Semester assignment", DatabaseExtractor.get_assessment_form("TMA4140"))

    def test_get_term(self):
        self.assertEqual("Spring", DatabaseExtractor.get_term("TMA4105"))
        self.assertEqual("Autumn", DatabaseExtractor.get_term("TMA4140"))
        self.assertEqual("Spring", DatabaseExtractor.get_term("TDT4145"))

    def test_get_year(self):
        self.assertEqual(2017, DatabaseExtractor.get_year("TMR4230"))
        self.assertEqual(2016, DatabaseExtractor.get_year("TMA4140"))

    def test_get_is_active_course_active(self):
        self.assertEqual(True, DatabaseExtractor.get_is_active_course("TTK4135"))
        self.assertEqual(True, DatabaseExtractor.get_is_active_course("TTK4105"))

    def test_get_is_active_course_notactive(self):
        self.assertEqual(False, DatabaseExtractor.get_is_active_course("TDT4120"))
        self.assertEqual(False, DatabaseExtractor.get_is_active_course("TMA4140"))
        self.assertEqual(False, DatabaseExtractor.get_is_active_course("TMA4100"))

    #OK
    def test_get_contact_name(self):
        self.assertEqual("The name of the contact person in TMR4105 Marine Technology - Elementary Course is Håvard Holm", DatabaseExtractor.get_contact_name("TMR4105"))
        self.assertEqual("The name of the contact person in TTK4105 Control Systems is Trond Andresen", DatabaseExtractor.get_contact_name("TTK4105"))
        self.assertEqual("The name of the contact person in TDT4140 Software Engineering is Pekka Kalevi Abrahamsson", DatabaseExtractor.get_contact_name("TDT4140"))

    #OK
    def test_get_contact_mail(self):
        self.assertEqual("The mail address of the contact person in TDT4140 Software Engineering is pekka.abrahamsson@ntnu.no", DatabaseExtractor.get_contact_mail("TDT4140"))
        self.assertEqual("The mail address of the contact person in TMA4115 Calculus 3 is aslak.buan@ntnu.no", DatabaseExtractor.get_contact_mail("TMA4115"))

    #OK
    def test_get_contact_office_exists(self):
        self.assertEqual("The office address of the contact person in TMA4105 Calculus 2 is Alfred Getz vei 1, Sentralbygg II * 1248", DatabaseExtractor.get_contact_office("TMA4105"))
        self.assertEqual("The office address of the contact person in TDT4145 Data Modelling, Databases and Database Management Systems is Sem Sælands vei 9, IT-bygget * 209", DatabaseExtractor.get_contact_office("TDT4145"))

    #OK
    def test_get_contact_office_notexists(self):
        self.assertEqual("There is no existing office address in TTK4115 Linear System Theory", DatabaseExtractor.get_contact_office("TTK4115"))

    #OK
    def test_get_contact_phone_exists(self):
        self.assertEqual("The phone number of the contact person in TDT4145 Data Modelling, Databases and Database Management Systems is 73550382", DatabaseExtractor.get_contact_phone("TDT4145"))
        self.assertEqual("The phone number of the contact person in TTK4105 Control Systems is 73594358", DatabaseExtractor.get_contact_phone("TTK4105"))

    #OK
    def test_get_contact_phone_notexists(self):
        self.assertEqual("There is no phone number available in TTK4115 Linear System Theory", DatabaseExtractor.get_contact_phone("TTK4115"))


    #OK
    def test_get_course_name(self):
        self.assertEqual("The course name is TDT4140 Software Engineering", DatabaseExtractor.get_course_name("TDT4140"))
        self.assertEqual("The course name is TMA4100 Calculus 1", DatabaseExtractor.get_course_name("TMA4100"))
        self.assertEqual("The course name is TTK4105 Control Systems", DatabaseExtractor.get_course_name("TTK4105"))
        self.assertEqual("The course name is TKT4124 Mechanics 3", DatabaseExtractor.get_course_name("TKT4124"))

    #OK
    def test_getCredit(self):
        self.assertEqual("The course TMA4100 Calculus 1 is 7.5 credits.", DatabaseExtractor.get_credit("TMA4100"))
        self.assertEqual("The course TMA4160 Cryptography is 7.5 credits.", DatabaseExtractor.get_credit("TMA4160"))
        self.assertEqual("The course IØ1000 Leadership in a Practical Context is 15 credits.", DatabaseExtractor.get_credit("IØ1000"))
        self.assertEqual("The course TMA4130 Calculus 4N is 7.5 credits.", DatabaseExtractor.get_credit("TMA4130"))
        self.assertEqual("The course TEP4100 Fluid Mechanics is 7.5 credits.", DatabaseExtractor.get_credit("TEP4100"))

    #OK
    def test_get_url_exists(self):
        self.assertEqual("http://wiki.math.ntnu.no/tma4105", DatabaseExtractor.get_url("TMA4105"))
        self.assertEqual("http://wiki.math.ntnu.no/tma4115", DatabaseExtractor.get_url("TMA4115"))

    #OK
    def test_get_url_notexists(self):
        self.assertEqual("Course url not available.", DatabaseExtractor.get_url("TMR4160"))
        self.assertEqual("Course url not available.", DatabaseExtractor.get_url("TTK4105"))

    #OK
    def test_get_prereq_knowledge_exists(self):
        self.assertEqual("Knowledge and skills equivalent to TDT4100 Object-Oriented Programming and TDT4120 "
                         "Algorithms and Data Structures. Java is used as the programming language in "
                         "projects and exercises.", DatabaseExtractor.get_prereq_knowledge("TDT4145"))
        self.assertEqual("TMA4100 Calculus 1 or equivalent.", DatabaseExtractor.get_prereq_knowledge("TMA4115"))
        self.assertEqual("TKT4116/TKT4118 Mechanics 1. ", DatabaseExtractor.get_prereq_knowledge("TKT4123"))
        self.assertEqual("TMA4100 Calculus 1.", DatabaseExtractor.get_prereq_knowledge("TKT4116"))

    #OK
    def test_get_prereq_knowledge_notexists(self):
        self.assertEqual("Prerequisite knowledge is not available for this course.", DatabaseExtractor.get_prereq_knowledge("TMA4100"))
        self.assertEqual("None.", DatabaseExtractor.get_prereq_knowledge("TDT4105"))


    def test_get_course_content(self):
        self.assertEqual("Curves in space. Functions of several variables. Taylor's theorem in two dimensions, extremal values in several variables, Lagrange multipliers. Double and triple integrals, line and surface integrals. Vector calculus. The theorems of Green, Stokes, and Gauss.", DatabaseExtractor.get_course_content("TMA4105"))
        self.assertEqual("Statically determinate structures: Beams, plane trusses and frames. Axial force, "
                         "shear force and bending moment distribution in structures. Introduction to mechanics of "
                         "materials: Stress, strain and elasticity. Linear theory for beams: Bending stresses, "
                         "differential equation for deformation of beams.", DatabaseExtractor.get_course_content("TKT4116"))
        self.assertEqual("Theory for linear multivariable systems, state space models, discretization, "
                         "canonical forms and realizations, Lyapunov stability, controllability and observability, "
                         "state feedback, LQ control, state estimation, the Kalman filter, descriptions of stochastic "
                         "processes and random signals.\r\n", DatabaseExtractor.get_course_content("TTK4115"))


    def test_get_course_material(self):
        self.assertEqual("Information will be given when the course starts.", DatabaseExtractor.get_course_material("TTK4115"))
        #self.assertEqual("Will be announced at the start of the course."", DatabaseExtractor.get_course_material("TMA4100"))
        #self.assertEqual("Konstruksjonsmekanikk, Del 1-Likevektslære, Fagbokforlaget.\r\nKonstruksjonsmekanikk, Del 2-Fasthetslære, Fagbokforlaget.\r\n", DatabaseExtractor.get_course_material("TKT4123"))

    def test_get_teaching_form(self):
        self.assertEqual("Lectures and exercises.", DatabaseExtractor.get_teaching_form("TMR4160"))
        self.assertEqual("The themes are illustrated through lectures, assignments, laboratory activities and project "
                         "work. Portfolio assessment is the basis for the grade in the course. The portfolio includes "
                         "a final oral exam and multiple choice (60%) and a design project report (40%). The results "
                         "for the parts are given in %-scores, while the entire portfolio is assigned a letter grade. "
                         "The course will also include mandatory courses in basic occupational safety and health (OSH)"
                         " and in practical work operations.", DatabaseExtractor.get_teaching_form("TMR4105"))





