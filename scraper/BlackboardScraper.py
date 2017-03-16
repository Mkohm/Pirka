from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui

# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html

# TODO: When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these varibles and make them member varibales in the class below if needed @Kohm?
chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_profile)
driver.get("https://ntnu.blackboard.com/")

class BlackboardScraper:
    def __init__(self):

        # TODO: add functionality for user credentials as parameters, not hardcoded like it is now
        # Hardcoding is only for testing purposes.

        # self.username = username
        # self.password = password

        login_button = driver.find_elements_by_class_name("loginPrimary")
        login_button[0].click()

        select = Select(driver.find_element_by_name('org'))

        select.select_by_visible_text("NTNU")

        driver.find_element_by_class_name("submit").click()

        # logs into Its Learning. After this the "driver" contains the main page in Its Learning
        username = driver.find_element_by_name("feidename")
        username.send_keys("evenkal") # TODO: add your own user name if you want to test
        password = driver.find_element_by_name("password")
        password.send_keys("") # TODO: add your own password if you want to test
        password.submit()


    # this function returns a users calendar feed in iCalendar-format
    # TODO: add functionality to extract the content from the feed
    def get_calendar_feed(self):

        # navigates to the calendar page in BB.
        driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool")
        driver.implicitly_wait(5)
        driver.find_element_by_id("ical")

        # # navigates to the body frame to be able to navigate further
        # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        #
        # # expand the menu button (with three dots) above the calender, on the right side of the page
        # cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_PageFunctions")
        # cal.click()
        #
        # # clicks the "abonner" butting
        # cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_ctl03_SubscribeLink")
        # cal.click()
        #
        # # extracts the calendar feed url and returns it as a string
        #
        # # TODO: This URL structure can be used to subscribe to a calendar by URL, implement feature
        # # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics
        #
        # return driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink").text


    def get_course_list(self):

        driver.implicitly_wait(5)
        class_table = driver.find_elements_by_id("_3_1termCourses_noterm")

        print(class_table[0].text)

    def get_first_course(self):

        driver.implicitly_wait(5)

        courses = driver.find_elements_by_partial_link_text(" /webapps/blackboard/execute/launcher?type=Course&id=")
        courses[0].click()

    def get_completed_assignments(self):

        driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=MyGradesOnMyBb_____MyGradesTool")
        driver.implicitly_wait(10)
        grades = driver.find_element_by_id("grade")

        print(grades[0].text)


    def close_driver(self):
        driver.quit()

myScrape = BlackboardScraper()

myScrape.get_first_course()

myScrape.get_completed_assignments()

myScrape.get_course_list()



# myScrape.get_calendar_feed()

