from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import platform
from database import DatabaseInserter


class BlackboardScraper:
    def __init__(self, username, password):
        """
        This method sets up scraper, and logs in to Blackboard. It enables the other methods to scrape
        content, like calendar feed, exercises and course list.
        :param username: FEIDE-username
        :param password: FEIDE-password
        """

        self.username = username
        self.password = password

        driver_directory = os.path.dirname(__file__)
        if platform.system() == "Windows":
            relative_path = "chromedriver.exe"
        else:
            relative_path = "chromedriver"
        absolute_file_path = os.path.join(driver_directory, relative_path)

        chrome_profile = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=absolute_file_path)
        self.driver.get("https://ntnu.blackboard.com/")

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

        # necessary data to locate the course list, which is essential to the rest of the scraping.
        # TODO: Make a method the compute the current term, in opposition to hard coding
        self.current_term = "(2017 VÅR)"
        self.course_list = self.get_course_list()

    # this function returns a users calendar feed in iCalendar-format
    def get_calendar_feed(self):
        """
        Should scrape BB to find, and extract, a calendar feed link, and then instert
        into the database. For some unknown reason this code has worked flawlessly earlier,
        but is not working now.
        :return: Returns a web link to an .ics file
        """

        # navigates to the calendar page in BB.
        self.driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool")
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_id("ical").click()
        ical_url = self.driver.find_element_by_id("icalurlid").text

<<<<<<< HEAD
        try:
            self.driver.find_element_by_class_name("fc-button-content.fc-button-main.fc-button-img").click()
            self.driver.find_element_by_class_name("fc-button-content.fc-button-main.fc-button-img").click()
        except:
            pass
        try:
            button = self.driver.find_element_by_id("ical")
        except:
            print("fail1")
            try:
                button = self.driver.find_element_by_xpath('//*[@id="ical"]')
            except:
                print("fail1.1")
                try:
                    button = self.driver.find_element_by_class_name("ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only")
                except:
                    print("fail1.2")
        try:
            button.click()
        except:
            print("fail2")
        try:
            ical_url = self.driver.find_element_by_id("icalurlid")
        except:
            print("fail3")
        print("test3")
=======
>>>>>>> origin/dev
        # This URL structure can be used to subscribe to a calendar by URL, implement feature
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics

        DatabaseInserter.add_blackboard_url(ical_url)
        return ical_url

    def get_course_list(self):
        """
        This method scrapes BB to get all the users active courses, and then
        stores it in the database.
        :return: course_list, a list of all the users active courses on BB.
        """

        # makes sure the page is completed loaded before trying to locate elements.
        self.driver.implicitly_wait(1)
        # utilize the fact that every link text for active courses contains the current term
        courses = self.driver.find_elements_by_partial_link_text(self.current_term)
        course_list = []

        for course in courses:
            course_list.append(course.text.split()[0])
            DatabaseInserter.add_user_has_course(self.username, str(course.text.split()[0]))

        return course_list

    def get_assignments(self, index):
        """
        Iterates through all assignments for the course placed at index 'course_index' in the
        users course list on Blackboard
        :param index: Index of the course the assignment is scraped from.
        :return:
        """
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
                score = self.driver.find_element_by_id("aggregateGrade").get_attribute("value")
                print(score)
                # For now, this is the only method to assure that not loads of bad data, like assignments instructions
                # and answer files, is added to the database.
                DatabaseInserter.add_assignment_data(course_code, title, i, True, None, None,
                                                     "its", "exercise", " ingen ")
                DatabaseInserter.add_user_completed_assignment(self.username, course_code, i + 1, "exercise", score)
            except:
                print("Score not available")

            # makes the driver ready for a new iteration
            self.driver.back()
            assignments = self.driver.find_elements_by_partial_link_text("Øving")

    def get_all_assignments(self):
        """
        This method loops through every course a user has on Blackboard, and then calls on
        self.get_assignments() to scrape all assignment data for each course and insert into the
        database
        """
        for i in range(0, len(self.course_list)):
            self.get_assignments(i)

    def close_driver(self):
        """
        When this class is intialized a new instance of Selenium webscraper is created. Of performance and reliability
         issues this scraper need to be termintad, which is what this method handles.
        """
        self.driver.quit()

