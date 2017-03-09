from unittest import TestCase
from imeapi.Course import Course

class TestCourse(TestCase):

    def test_get_exam_date_ok_input(self):
        self.assertEqual(Course("TDT4100").get_exam_date(), "Exam date for TDT4100 Object-Oriented Programming is May 16, 2017")
        self.assertEqual(Course("TFE4120").get_exam_date(), "Exam date for TFE4120 Electromagnetics is May 29, 2017")
        self.assertEqual(Course("TTK4135").get_exam_date(), "Exam date for TTK4135 Optimization and Control is May 20, 2017")

    def test_get_exam_date_no_exam(self):
        self.assertEqual("No exam date available because assessment form is: Work", Course("TDT4140").get_exam_date())
        self.assertEqual("No exam date available because assessment form is: Work", Course("TMR4160").get_exam_date())

    def test_get_exam_date_wrong_input(self):
        self.assertEqual(Course("TMR1111").get_exam_date(), "You entered an invalid course code.")
        self.assertEqual(Course("jflsh").get_exam_date(), "You entered an invalid course code.")

    def test_get_exam_date_course_not_active(self):
        self.assertEqual("No exam date available because the course is not active.", Course("TMA4100").get_exam_date())
        self.assertEqual("No exam date available because the course is not active.", Course("TMA4140").get_exam_date())

    def test_assessment_form_written(self):
        self.assertEqual("Written examination", Course("TDT4100").get_assessment_form())
        self.assertEqual("Written examination", Course("TMA4140").get_assessment_form())

    def test_assessment_form_work(self):
        self.assertEqual("Work", Course("TDT4140").get_assessment_form())
        self.assertEqual("Work", Course("TMR4160").get_assessment_form())

    def test_assessment_form_combination(self):
        self.assertEqual(Course("TTK4135").get_assessment_form(), "Written examination and Work and Semester assignment")
        self.assertEqual(Course("TMR4105").get_assessment_form(), "Work and Oral examination")
        self.assertEqual(Course("TMR4230").get_assessment_form(), "Oral examination and Semester assignment")

    def test_get_term(self):
        self.assertEqual("Spring", Course("TMA4105").get_term())
        self.assertEqual("Autumn", Course("TMA4140").get_term())
        self.assertEqual("Spring", Course("TDT4145").get_term())

    def test_get_year(self):
        self.assertEqual(2017, Course("TMR4230").get_year())
        self.assertEqual(2016, Course ("TMA4140").get_year())

    def test_get_is_active_course_active(self):
        self.assertEqual(True, Course("TTK4135").get_is_active_course())
        self.assertEqual(True, Course("TTK4105").get_is_active_course())

    def test_get_is_active_course_notactive(self):
        self.assertEqual(False, Course("TDT4120").get_is_active_course())
        self.assertEqual(False, Course("TMA4140").get_is_active_course())
        self.assertEqual(False, Course("TMA4100").get_is_active_course())

    def test_get_contact_name(self):
        self.assertEqual("Håvard Holm", Course("TMR4105").get_contact_name())
        self.assertEqual("Trond Andresen", Course("TTK4105").get_contact_name())
        self.assertEqual("Pekka Kalevi Abrahamsson", Course("TDT4140").get_contact_name())

    def test_get_contact_mail(self):
        self.assertEqual("pekka.abrahamsson@ntnu.no", Course("TDT4140").get_contact_mail())
        self.assertEqual("aslak.buan@ntnu.no", Course("TMA4115").get_contact_mail())

    def test_get_contact_office_exists(self):
        self.assertEqual("Alfred Getz vei 1, Sentralbygg II * 1248", Course("TMA4105").get_contact_office())
        self.assertEqual("Sem Sælands vei 9, IT-bygget * 209", Course("TDT4145").get_contact_office())

    def test_get_contact_office_notexists(self):
        self.assertEqual("Office address is not available", Course("TTK4115").get_contact_office())

    def test_get_contact_phone_exists(self):
        self.assertEqual("73550382", Course("tdt4145").get_contact_phone())
        self.assertEqual("73594358", Course("ttk4105").get_contact_phone())

    def test_get_contact_phone_notexists(self):
        self.assertEqual("Contact phone is not available", Course("TTK4115").get_contact_phone())

    def test_get_contact_website_exists(self):
        self.assertEqual("https://www.ntnu.no/ansatte/trond.andresen", Course("ttk4105").get_contact_website())
        self.assertEqual("https://www.ntnu.no/ansatte/morten.d.pedersen", Course("ttk4115").get_contact_website())
        self.assertEqual("https://www.ntnu.no/ansatte/haavard.holm", Course("tmr4105").get_contact_website())

    def test_get_course_name(self):
        self.assertEqual("Software Engineering", Course("TDT4140").get_course_name())
        self.assertEqual("Calculus 1", Course("TMA4100").get_course_name())
        self.assertEqual("Control Systems", Course("TTK4105").get_course_name())
        self.assertEqual("Mechanics 3", Course("TKT4124").get_course_name())
        #following tests are removed because the invalid course-checker will be in api.ai
        #self.assertEqual(Course.get_course_name("fgyjhkdlsø"), "Invalid course")
        #self.assertEqual(Course.get_course_name("TMR1111"), "Invalid course")

    def test_getCredit(self):
        self.assertEqual(7.5, Course("TMA4100").get_credit())
        self.assertEqual(7.5, Course("TMA4160").get_credit())
        self.assertEqual(15.0, Course("IØ1000").get_credit())
        self.assertEqual(7.5, Course("TMA4130").get_credit())
        self.assertEqual(7.5, Course("TEP4100").get_credit())

    def test_get_url_exists(self):
        self.assertEqual("http://wiki.math.ntnu.no/tma4105", Course("TMA4105").get_url())
        self.assertEqual("http://wiki.math.ntnu.no/tma4115", Course("TMA4115").get_url())

    def test_get_url_notexists(self):
        self.assertEqual("Course url not available", Course("TMR4160").get_url())
        self.assertEqual("Course url not available", Course("TTK4105").get_url())

    def test_get_prereq_knowledge_exists(self):
        self.assertEqual("Knowledge and skills equivalent to TDT4100 Object-Oriented Programming and TDT4120 "
                         "Algorithms and Data Structures. Java is used as the programming language in "
                         "projects and exercises.", Course("TDT4145").get_prereq_knowledge())
        self.assertEqual("TMA4100 Calculus 1 or equivalent.", Course("TMA4115").get_prereq_knowledge())
        self.assertEqual("TKT4116/TKT4118 Mechanics 1. ", Course("TKT4123").get_prereq_knowledge())

    def test_get_prereq_knowledge_notexists(self):
        self.assertEqual("Prerequisite knowledge is not available for this course",
                         Course("TMA4100").get_prereq_knowledge())
        self.assertEqual("Prerequisite knowledge is not available for this course",
                         Course("TDT4105").get_prereq_knowledge())
        self.assertEqual("Prerequisite knowledge is not available for this course",
                         Course("").get_prereq_knowledge("TKT4116"))

    def test_get_course_content(self):
        self.assertEqual("Curves in space. Functions of several variables. Taylor's theorem in two dimensions, "
                         "extremal values in several variables, Lagrange multipliers. Double and triple integrals, "
                         "line and surface integrals. Vector calculus. The theorems of Green, Stokes, and Gauss.",
                         Course("TMA4105").get_course_content())
        self.assertEqual("Statically determinate structures: Beams, plane trusses and frames. Axial force, "
                         "shear force and bending moment distribution in structures. Introduction to mechanics of "
                         "materials: Stress, strain and elasticity. Linear theory for beams: Bending stresses, "
                         "differential equation for deformation of beams.", Course("TKT4116").get_course_content())
        self.assertEqual("Theory for linear multivariable systems, state space models, discretization, "
                         "canonical forms and realizations, Lyapunov stability, controllability and observability, "
                         "state feedback, LQ control, state estimation, the Kalman filter, descriptions of stochastic "
                         "processes and random signals. ", Course("TTK4115").get_course_content())


    def test_get_course_material(self):
        self.assertEqual("Information will be given when the course starts.", Course("TTK4115").get_course_material())
        self.assertEqual("Will be announced at the start of the course.", Course("TMA4100").get_course_material())
        self.assertEqual("Konstruksjonsmekanikk, Del 1-Likevektslære, Fagbokforlaget. Konstruksjonsmekanikk, "
                         "Del 2-Fasthetslære, Fagbokforlaget. ", Course("TKT4123").get_course_material())

    def test_get_teaching_form(self):
        self.assertEqual("Lectures and exercises.", Course("TMR4160").get_teaching_form())
        self.assertEqual("The themes are illustrated through lectures, assignments, laboratory activities and project "
                         "work. Portfolio assessment is the basis for the grade in the course. The portfolio includes "
                         "a final oral exam and multiple choice (60%) and a design project report (40%). The results "
                         "for the parts are given in %-scores, while the entire portfolio is assigned a letter grade. "
                         "The course will also include mandatory courses in basic occupational safety and health (OSH)"
                         " and in practical work operations.", Course("TMR4105").get_teaching_form())





