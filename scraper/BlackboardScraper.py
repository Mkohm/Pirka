from selenium import webdriver
from selenium.webdriver.support.ui import Select

# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html

# When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these varibles and make them member varibales in the class below if needed @Kohm?
chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_profile)
driver.get("https://ntnu.blackboard.com/")

class BlackboardScraper:
    def __init__(self):

        # TODO: add functionality for user credentials as parameters

        # self.username = username
        # self.password = password

        login_button = driver.find_elements_by_class_name("loginPrimary")
        login_button[0].click()

        select = Select(driver.find_element_by_name('org'))
        select.select_by_visible_text("NTNU")
        driver.find_element_by_class_name("submit").click()

        # logs into BB. After this the "driver" contains the main page in Its Learning
        username = driver.find_element_by_name("feidename")
        username.send_keys(input("Username: "))
        password = driver.find_element_by_name("password")
        password.send_keys(input("Password: "))
        password.submit()

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

        driver.implicitly_wait(5)
        class_table = driver.find_elements_by_id("_3_1termCourses_noterm")

        print(class_table[0].text)

    def get_first_course(self):

        current_term = "(2017 VÅR)"

        driver.implicitly_wait(2)

        courses = driver.find_elements_by_partial_link_text(current_term)
        courses[0].click()

        driver.find_element_by_id("menuPuller").click()

        assignments = driver.find_element_by_partial_link_text("Mine evaluering")
        assignments.click()




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

myScrape = BlackboardScraper()

# myScrape.get_first_course()

myScrape.get_completed_assignments()
#
# myScrape.get_course_list()

myScrape.close_driver()

# myScrape.get_calendar_feed()

