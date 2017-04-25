from unittest import TestCase
from scraper.ItsLearningScraper import ItsLearningScraper

class TestItsLearningScraper(TestCase):
    def setUp(self):
        #todo: Type in username and password for NTNU account to run this test
        self.username = "marihl"
        self.password = "Fyrstikk94"
        self.scraper = ItsLearningScraper(self.username, self.password)

    def test_get_course_list(self):
        try:
            self.scraper.get_course_list()
        except Exception:
            self.fail("get_course_list() raised an Exception")

    def test_get_assignments(self):
        try:
            self.scraper.get_assignments()
        except Exception:
            self.fail("get_assignments() raised an Exception")

    def test_get_all_assignments(self):
        try:
            self.scraper.get_all_assignments()
        except Exception:
            self.fail("get_all_assignments() raised an Exception")

    def test_get_announcements(self):
        try:
            self.scraper.get_announcements()
        except Exception:
            self.fail("get_announcements() raised an Exception")









