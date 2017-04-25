from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import platform
from database import DatabaseInserter



class BlackboardScraper:
    def __init__(self, username, password):

        driver_directory = os.path.dirname(__file__)
        if platform.system() == "Windows":
            relative_path = "chromedriver.exe"
        else:
            relative_path = "chromedriver"
        absolute_file_path = os.path.join(driver_directory, relative_path)

        chrome_profile = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=absolute_file_path)
        self.driver.get("https://ntnu.blackboard.com/")




        self.username = username
        self.password = password

        login_button = self.driver.find_elements_by_class_name("loginPrimary")
        login_button[0].click()

        select = Select(self.driver.find_element_by_name('org'))
        select.select_by_visible_text("NTNU")
        self.driver.find_element_by_class_name("submit").click()

        # logs into BB. After this the "driver" contains the main page in Its Learning
        username_field = self.driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()

        # necessary to locate the course list
        self.current_term = "(2017 VÅR)"
        self.course_list = self.get_course_list()

    # this function returns a users calendar feed in iCalendar-format
    def get_calendar_feed(self):

        # navigates to the calendar page in BB.
        self.driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool")
        self.driver.implicitly_wait(2)
        ical_url = self.driver.find_element_by_id("ical")

        # This URL structure can be used to subscribe to a calendar by URL, implement feature
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics

        DatabaseInserter.add_blackboard_url(ical_url)

    def get_course_list(self):

        # makes sure the page is completed loaded before trying to locate elements.
        self.driver.implicitly_wait(1)
        # utilize the fact that every link text for active courses contains the current term
        courses = self.driver.find_elements_by_partial_link_text(self.current_term)
        course_list = []

        for course in courses:
            course_list.append(course.text.split()[0])

        return course_list

    def get_assignments(self, index):
        self.driver.get("https://ntnu.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_70_1")
        courses = self.driver.find_elements_by_partial_link_text(self.current_term)

        course_code = courses[index].text.split()[0]

        print("Course: " + course_code)
        courses[index].click()

        try:
            assignment_folder = self.driver.find_element_by_partial_link_text("Øvinger")
            assignment_folder.click()
        except:
            self.driver.find_element_by_id("menuPuller").click()
            assignment_folder = self.driver.find_element_by_partial_link_text("Øvinger")
            assignment_folder.click()



        assignments = self.driver.find_elements_by_partial_link_text("Øving")

        # this is the number of html links which may lead to an assignment.
        number_of_links = len(assignments)

        # Iterates through all the the relevant links, and looks for pages containing assignments.
        # For some assignments the assignment instruction may be attached as a PDF with the same link text.
        # This causes problems for the scraper as it will open the PDF in a new window, and then try the go back to
        # the previous page, which clearly is not possible, ending with a stop in the scraping.
        for i in range(0, number_of_links):

            try:
                assignments = self.driver.find_element_by_partial_link_text("Øving " + str(i+1))
                title = assignments.text
                print("Title: " + title + " (" + course_code + ")")
            except:
                pass

            try:
                assignments.click()
            except:
                print("Bug")
            try:
                score = self.driver.find_element_by_id("aggregateGrade")
                print(score.get_attribute("value"))
            except:
                print("Score not available")
                score = None

            try:
                max_score = int(self.driver.find_element_by_id("aggregateGrade_pointsPossible").text)
            except:
                print("Max score not available")
                max_score = 0

            try:
                self.driver.back()
                print("going back")
            except:
                print("could not go back")


            # The only items which is uniquely identified as real assignments is, for now,
            # items where a max score exists. This is done to avoid bad data in the database.
            if max_score > 0:
                DatabaseInserter.add_assignment_data(course_code, title, i, True, None, None,
                                                     "its", "exercise", " ingen ")
                DatabaseInserter.add_user_completed_assignment(self.username, course_code, i + 1, "exercise", score)

            assignments = self.driver.find_elements_by_partial_link_text("Øving")

    def get_all_assignments(self):
        for i in range(0, len(self.course_list)):
            self.get_assignments(i)

    def close_driver(self):
        self.driver.quit()



