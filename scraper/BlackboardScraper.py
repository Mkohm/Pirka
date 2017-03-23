from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import platform

# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html
# When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these varibles and make them member varibales in the class below if needed @Kohm?
driver_directory = os.path.dirname(__file__)
if platform.system() == "Windows":
    relative_path = "chromedriver.exe"
else:
    relative_path = "chromedriver"
absolute_file_path = os.path.join(driver_directory, relative_path)

chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=absolute_file_path)
driver.get("https://ntnu.blackboard.com/")

class BlackboardScraper:
    def __init__(self, username, password):

        # TODO: add functionality for user credentials as parameters

        login_button = driver.find_elements_by_class_name("loginPrimary")
        login_button[0].click()

        select = Select(driver.find_element_by_name('org'))
        select.select_by_visible_text("NTNU")
        driver.find_element_by_class_name("submit").click()

        # logs into BB. After this the "driver" contains the main page in Its Learning
        username_field = driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()

        # necassary to locate the course list
        self.current_term = "(2017 VÅR)"

    # this function returns a users calendar feed in iCalendar-format
    # TODO: add functionality to extract the content from the feed
    def get_calendar_feed(self):

        # navigates to the calendar page in BB.
        driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool")
        driver.implicitly_wait(5)
        driver.find_element_by_id("ical")

        # TODO: implement the rest of this method

        # TODO: This URL structure can be used to subscribe to a calendar by URL, implement feature
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics



    def get_course_list(self):

        driver.implicitly_wait(1)
        courses = driver.find_elements_by_partial_link_text(self.current_term)

        course_list = []

        for course in courses:
            print(course.text[0:7])
            course_list.append(course.text[0:7])

        courses[0].click()

        return course_list

    def get_first_course(self):


        driver.implicitly_wait(2)

        courses = driver.find_elements_by_partial_link_text(self.current_term)
        courses[0].click()

        driver.find_element_by_id("menuPuller").click()

        assignments = driver.find_element_by_partial_link_text("Mine evaluering")
        driver.implicitly_wait(2)
        assignments.click()

        item = driver.find_elements_by_css_selector("div.cell.gradable")
        driver.implicitly_wait(2)
        timestamp = driver.find_elements_by_class_name("lastActivityDate")


        for i in range(1, len(item)):
            print("Item " + str(i) + "\n" + item[i].text)
            print("Timestamp: " + timestamp[i].text + "\n\n")


    def get_completed_assignments(self):

        driver.get("https://ntnu.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=MyGradesOnMyBb_____MyGradesTool")
        driver.implicitly_wait(5)

        driver.switch_to.frame("mybbCanvas")
        driver.switch_to.frame("right_stream_mygrades")

        # sorts the assignments by ascending deadlines.
        select = Select(driver.find_element_by_name('sortby'))
        select.select_by_visible_text("Innleveringsfrist (eldste først)")



        assignments = driver.find_elements_by_css_selector("div.cell.gradable")
        activity = driver.find_elements_by_class_name("activityType")
        category = driver.find_elements_by_class_name("itemCat")
        grades = driver.find_elements_by_class_name("grade")
        grade_score = driver.find_elements_by_css_selector("span.grade")


        for i in range(0, len(grade_score)):
            print("Index: " + str(i))
            print("\nAssignment: " +assignments[i+1].text)
            print("Activity: " +activity[i].text)
            try:
                print("Category: " + category[i].text)
                print("Grade: " + grades[i].text)
                print("Grade score: " + grade_score[i].text + "\n")
            except IndexError:
                print(" ")


    def close_driver(self):
        driver.quit()

user = "evenkal"
password = input("Password: ")

myScrape = BlackboardScraper(user, password)

# myScrape.get_first_course()

myScrape.get_completed_assignments()
#

# myScrape.get_first_course()

myScrape.close_driver()

# myScrape.get_calendar_feed()

