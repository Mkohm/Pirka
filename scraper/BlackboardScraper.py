from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from database import DatabaseInserter
import platform

# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html
# When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

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

        self.username = username
        self.password = password

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

        # necessary to locate the course list
        self.current_term = "(2017 VÅR)"
        self.course_list = self.get_course_list()

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
            course_list.append(course.text.split()[0])
            DatabaseInserter.add_user_has_course(self.username, str(course.text.split()[0]))


        return course_list


    def get_course(self, index):
        driver.get("https://ntnu.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_70_1")
        courses = driver.find_elements_by_partial_link_text(self.current_term)

        courses[index].click()

        driver.find_element_by_id("menuPuller").click()
        assignment_folder = driver.find_element_by_partial_link_text("Øvinger")
        assignment_folder.click()

    def get_assignments(self, index):
        driver.get("https://ntnu.blackboard.com/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_70_1")
        courses = driver.find_elements_by_partial_link_text(self.current_term)

        course_code = courses[index].text.split()[0]
        courses[index].click()

        try:
            assignment_folder = driver.find_element_by_partial_link_text("Øvinger")
        except:
            driver.find_element_by_id("menuPuller").click()
            assignment_folder = driver.find_element_by_partial_link_text("Øvinger")

        assignment_folder.click()
        assignments = driver.find_elements_by_partial_link_text("Øving")

        print("Trying to loop through the assignments")
        for i in range(0, len(assignments)):

            title = assignments[i].text
            obligatory = True
            published = None
            try:
                print("Title: " + title + " (" + course_code + ")")
                assignments[i].click()
                score = driver.find_element_by_id("aggregateGrade")
                print(score.get_attribute("value"))
                max_score = driver.find_element_by_id("aggregateGrade_pointsPossible")
                print(max_score.text)


                try:
                    details = driver.find_element_by_class_name("detailsHeader")
                    details.click()

                    info = driver.find_element_by_class_name("assignmentInfo")
                    print("\n\nInfo: " + info + "\n\n")
                    driver.back()
                except:
                    deadline = None
            except:
                print("Score not available")

            DatabaseInserter.add_assignment_data(course_code, title, i + 1, str(obligatory), published, deadline,
                                                     "its", "exercise", " ingen ")
            DatabaseInserter.add_user_completed_assignment(self.username, course_code, i + 1, "exercise", score)

            driver.back()
            assignments = driver.find_elements_by_partial_link_text("Øving")


    def get_all_assignments(self):

        for i in range(0, len(self.course_list)):
            self.get_assignments(i)

        # # item = driver.find_elements_by_css_selector("div.cell.gradable")
        # # driver.implicitly_wait(2)
        # # timestamp = driver.find_elements_by_class_name("lastActivityDate")
        # #
        # #
        # # for i in range(1, len(item)):
        # #     print("Item " + str(i) + "\n" + item[i].text)
        # #     print("Timestamp: " + timestamp[i].text + "\n\n")
        #
        # print("Course: " + current_course)
        # courses[index].click()
        #
        # # driver.find_element_by_id("menuPuller").click()
        #
        # assignment_folder = driver.find_element_by_partial_link_text("Øvinger")
        # assignment_folder.click()
        #
        # assignments = driver.find_elements_by_partial_link_text("Øving")
        # print("Num of assign: " + str(len(assignments)))
        #
        #
        # for i in range(1, len(assignments)):
        #
        #     print("\nLooking for link 'Øving " + str(i) + "'")
        #
        #     try:
        #         assignment = driver.find_element_by_partial_link_text("Øving " + str(i))
        #         title = assignment.text
        #         print("Title: " + title + " (" + current_course + ", i=" + str(i) + ")")
        #         assignment.click()
        #         try:
        #             score = driver.find_element_by_id("aggregateGrade")
        #             print(score.get_attribute("value"))
        #         except:
        #             print("Score not available")
        #         max_score = driver.find_element_by_id("aggregateGrade_pointsPossible")
        #         print(max_score.text)
        #         driver.back()
        #     except:
        #         print("Exercise info not available")
        #         driver.back()
        #
        # assignments = driver.find_elements_by_css_selector("sortable.item_row.graded_item_row.row.expanded")
        #
        # assignment = assignments[0]
        # grade = assignment.get_attribute("grade")
        # print("Grade: " + grade)
        #
        #
        #
        # # activity = driver.find_elements_by_class_name("activityType")
        # # category = driver.find_elements_by_class_name("itemCat")
        # # grades = driver.find_elements_by_class_name("grade")
        # # grade_score = driver.find_elements_by_css_selector("span.grade")
        # #
        # #
        # # for i in range(0, len(grade_score)):
        # #     print("Index: " + str(i))
        # #     print("\nAssignment: " +assignments[i+1].text)
        # #     print("Activity: " +activity[i].text)
        # #     try:
        # #         print("Category: " + category[i].text)
        # #         print("Grade: " + grades[i].text)
        # #         print("Grade score: " + grade_score[i].text + "\n")
        # #     except IndexError:
        # #         print(" ")


    def close_driver(self):
        driver.quit()


"""

user = "evenkal"
password = input("Password: ")
myScrape = BlackboardScraper(user, password)



try:
    myScrape.get_all_assignments()

    # myScrape.get_completed_assignments()
except:
    print("failed")


myScrape.close_driver()

# myScrape.get_calendar_feed()


"""

