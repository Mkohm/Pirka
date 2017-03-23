from unittest import TestCase

from database import DatabaseExtractor

class TestCourse(TestCase):

    def test_get_exam_date_ok_input(self):
        self.assertEqual("Exam date for TDT4100 Object-Oriented Programming is May 16, 2017", DatabaseExtractor.get_exam_date("TDT4100"))
        self.assertEqual("Exam date for TFE4120 Electromagnetics is May 29, 2017", DatabaseExtractor.get_exam_date("TFE4120"))
        self.assertEqual("Exam date for TTK4135 Optimization and Control is May 20, 2017", DatabaseExtractor.get_exam_date("TTK4135"))

    def test_get_exam_date_no_exam(self):
        self.assertEqual("No exam date available because assessment form is: Work", DatabaseExtractor.get_exam_date("TDT4140"))
        self.assertEqual("No exam date available because assessment form is: Work", DatabaseExtractor.get_exam_date("TMR4160"))

    def test_get_exam_date_wrong_input(self):
        self.assertEqual("You entered an invalid course code.", DatabaseExtractor.get_exam_date("TMR1111"))
        self.assertEqual("You entered an invalid course code.", DatabaseExtractor.get_exam_date("jflsh"))

    def test_get_exam_date_course_not_active(self):
        self.assertEqual("No exam date available because the course is not active.", DatabaseExtractor.get_exam_date("TMA4100"))
        self.assertEqual("No exam date available because the course is not active.", DatabaseExtractor.get_exam_date("TMA4140"))

    def test_assessment_form_written(self):
        self.assertEqual("Written examination", DatabaseExtractor.get_assessment_form("TDT4100"))
        self.assertEqual("Written examination", DatabaseExtractor.get_assessment_form("TDT4105"))

    def test_assessment_form_work(self):
        self.assertEqual("Work", DatabaseExtractor.get_assessment_form("TDT4140"))
        self.assertEqual("Work", DatabaseExtractor.get_assessment_form("TMR4160"))

    def test_assessment_form_combination(self):
        self.assertEqual("Written examination and Work and Semester assignment", DatabaseExtractor.get_assessment_form("TTK4135"))
        self.assertEqual("Work and Oral examination", DatabaseExtractor.get_assessment_form("TMR4105"))
        self.assertEqual("Oral examination and Semester assignment", DatabaseExtractor.get_assessment_form("TMR4230"))
        self.assertEqual("Written examination and Semester assignment", DatabaseExtractor.get_assessment_form("TMA4140"))

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

    def test_get_contact_name(self):
        self.assertEqual("Håvard Holm", DatabaseExtractor.get_contact_name("TMR4105"))
        self.assertEqual("Trond Andresen", DatabaseExtractor.get_contact_name("TTK4105"))
        self.assertEqual("Pekka Kalevi Abrahamsson", DatabaseExtractor.get_contact_name("TDT4140"))

    def test_get_contact_mail(self):
        self.assertEqual("pekka.abrahamsson@ntnu.no", DatabaseExtractor.get_contact_mail("TDT4140"))
        self.assertEqual("aslak.buan@ntnu.no", DatabaseExtractor.get_contact_mail("TMA4115"))

    def test_get_contact_office_exists(self):
        self.assertEqual("Alfred Getz vei 1, Sentralbygg II * 1248", DatabaseExtractor.get_contact_office("TMA4105"))
        self.assertEqual("Sem Sælands vei 9, IT-bygget * 209", DatabaseExtractor.get_contact_office("TDT4145"))

    def test_get_contact_office_notexists(self):
        self.assertEqual("Office address is not available", DatabaseExtractor.get_contact_office("TTK4115"))

    def test_get_contact_phone_exists(self):
        self.assertEqual("73550382", DatabaseExtractor.get_contact_phone("TDT4145"))
        self.assertEqual("73594358", DatabaseExtractor.get_contact_phone("TTK4105"))

    def test_get_contact_phone_notexists(self):
        self.assertEqual("Contact phone is not available", DatabaseExtractor.get_contact_phone("TTK4115"))

    def test_get_contact_website_exists(self):
        self.assertEqual("https://www.ntnu.no/ansatte/trond.andresen", DatabaseExtractor.get_contact_website("TTK4105"))
        self.assertEqual("https://www.ntnu.no/ansatte/morten.d.pedersen", DatabaseExtractor.get_contact_website("TTK4115"))
        self.assertEqual("https://www.ntnu.no/ansatte/haavard.holm", DatabaseExtractor.get_contact_website("TMR4105"))

    def test_get_course_name(self):
        self.assertEqual("Software Engineering", DatabaseExtractor.get_course_name("TDT4140"))
        self.assertEqual("Calculus 1", DatabaseExtractor.get_course_name("TMA4100"))
        self.assertEqual("Control Systems", DatabaseExtractor.get_course_name("TTK4105"))
        self.assertEqual("Mechanics 3", DatabaseExtractor.get_course_name("TKT4124"))


    def test_getCredit(self):
        self.assertEqual(7.5, DatabaseExtractor.get_credit("TMA4100"))
        self.assertEqual(7.5, DatabaseExtractor.get_credit("TMA4160"))
        self.assertEqual(15.0, DatabaseExtractor.get_credit("IØ1000"))
        self.assertEqual(7.5, DatabaseExtractor.get_credit("TMA4130"))
        self.assertEqual(7.5, DatabaseExtractor.get_credit("TEP4100"))

    def test_get_url_exists(self):
        self.assertEqual("http://wiki.math.ntnu.no/tma4105", DatabaseExtractor.get_url("TMA4105"))
        self.assertEqual("http://wiki.math.ntnu.no/tma4115", DatabaseExtractor.get_url("TMA4115"))

    def test_get_url_notexists(self):
        self.assertEqual("Course url not available", DatabaseExtractor.get_url("TMR4160"))
        self.assertEqual("Course url not available", DatabaseExtractor.get_url("TTK4105"))

    def test_get_prereq_knowledge_exists(self):
        self.assertEqual("Knowledge and skills equivalent to TDT4100 Object-Oriented Programming and TDT4120 "
                         "Algorithms and Data Structures. Java is used as the programming language in "
                         "projects and exercises.", DatabaseExtractor.get_prereq_knowledge("TDT4145"))
        self.assertEqual("TMA4100 Calculus 1 or equivalent.", DatabaseExtractor.get_prereq_knowledge("TMA4115"))
        self.assertEqual("TKT4116/TKT4118 Mechanics 1. ", DatabaseExtractor.get_prereq_knowledge("TKT4123"))
        self.assertEqual("TMA4100 Calculus 1.", DatabaseExtractor.get_prereq_knowledge("TKT4116"))

    def test_get_prereq_knowledge_notexists(self):
        self.assertEqual("Prerequisite knowledge is not available for this course", DatabaseExtractor.get_prereq_knowledge("TMA4100"))
        self.assertEqual("None.", DatabaseExtractor.get_prereq_knowledge("TDT4105"))


    def test_get_course_content(self):
        self.assertEqual("Curves in space. Functions of several variables. Taylor's theorem in two dimensions, "
                         "extremal values in several variables, Lagrange multipliers. Double and triple integrals, "
                         "line and surface integrals. Vector calculus. The theorems of Green, Stokes, and Gauss.",
                         DatabaseExtractor.get_course_content("TMA4105"))
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
        self.assertEqual("Will be announced at the start of the course.", DatabaseExtractor.get_course_material("TMA4100"))
        self.assertEqual("Konstruksjonsmekanikk, Del 1-Likevektslære, Fagbokforlaget. Konstruksjonsmekanikk, "
                         "Del 2-Fasthetslære\r, Fagbokforlaget. ", DatabaseExtractor.get_course_material("TKT4123"))

    def test_get_teaching_form(self):
        self.assertEqual("Lectures and exercises.", DatabaseExtractor.get_teaching_form("TMR4160"))
        self.assertEqual("The themes are illustrated through lectures, assignments, laboratory activities and project "
                         "work. Portfolio assessment is the basis for the grade in the course. The portfolio includes "
                         "a final oral exam and multiple choice (60%) and a design project report (40%). The results "
                         "for the parts are given in %-scores, while the entire portfolio is assigned a letter grade. "
                         "The course will also include mandatory courses in basic occupational safety and health (OSH)"
                         " and in practical work operations.", DatabaseExtractor.get_teaching_form("TMR4105"))





