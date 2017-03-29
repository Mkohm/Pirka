from selenium import webdriver
import os
import platform
from database import DatabaseInserter

# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html
# When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these variables and make them member variables in the class below if needed?

driver_directory = os.path.dirname(__file__)
if(platform.system() == "Windows"):
    relative_path = "chromedriver.exe"
else:
    relative_path = "chromedriver"
absolute_file_path = os.path.join(driver_directory, relative_path)

chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=absolute_file_path)
driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning

class tempScraper:
    def __init__(self, username, password):
        # TODO: add functionality for user credentials as parameters

        self.username = username
        self.password = password

        # logs into Its Learning. After this the "driver" contains the main page in Its Learning
        username_field = driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()

    @staticmethod
    def login(username, password):
        username_field = driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()
        driver.close()


    # this function returns a users calendar feed in iCalendar-format
    # TODO: add functionality to extract the content from the feed
    def get_calendar_feed(self):

        # navigates to the calendar page in Its Learning.
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Calendar%2fSchedule.aspx&Item=l-menu-calendar")

        # navigates to the body frame to be able to navigate further
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # expand the menu button (with three dots) above the calender, on the right side of the page
        cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_PageFunctions")
        cal.click()

        # clicks the "abonner" butting
        cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_ctl03_SubscribeLink")
        cal.click()

        # extracts the calendar feed url and returns it as a string

        # TODO: This URL structure can be used to subscribe to a calendar by URL, implement feature
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics

        return driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink").text

    # returns the user course list as a list of strings
    # TODO: Write the result to database.user_has_subject


    def get_course_list(self):

        # gets the course overveiw page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

        course_list = []

        for course in courses:
            # '.text' extracts the text contained in the WebElement (which is what Selenium extracts)
            course_list.append(course.text)
            course_list.append(course.text)
            DatabaseInserter.add_user_has_course(self.username, str(course.text[0:7]))

        return course_list

    # Should be splitted into several methods, but have not found a solution that Selenium supports yet.
    def get_assignments(self, course_index):

        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

        # Navigates to the relevant course based in course index
        course_code = courses[course_index].text.split()[0]
        print("Extracting info from: " + course_code)
        courses[course_index].click()

        # Try to find a folder containing assignments
        try:
            link = driver.find_element_by_link_text("Assignments")
        except:
            try:
                link = driver.find_element_by_link_text("Øvinger")
            except:
                print("Unable to find assignments for " + course_code)
                return "Unable to find assignments for " + course_code

        link.click()
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        link = driver.find_elements_by_class_name("GridTitle")

        # loops through every element in the assignment folder, tries to extract info
        # TODO: store the values in the database
        for i in range(0, len(link)):
            link[i].click()

            try:
                title = driver.find_elements_by_class_name("ccl-pageheader-title")[0].text
                attribute = driver.find_elements_by_class_name("h-mrb5")

                published = attribute[0].text[11:]
                deadline = attribute[1].text[11:]

                if ("Ja" in attribute[2].text):
                    obligatory = True
                else:
                    obligatory = False

                if ("Ja" in attribute[3].text):
                    anonymous = True
                else:
                    anonymous = False

                group = attribute[4].text[14:]

                print("Title: " + title)
                print("Published: " + published)
                print("Deadline: " + deadline)
                print("Obligatory: " + str(obligatory))
                print("Anonym: " + str(anonymous))
                print("Group: " + group)


                try:
                    assessment = driver.find_element_by_class_name("colorbox_green").text
                    print("Assessment: " + assessment)
                except:
                    print(" ")

                print(" ")

                if "Godkjent/Vurdert" in assessment:
                    score = 1
                else:
                    score = 0

                DatabaseInserter.add_assignment_data(course_code, title, i + 1, str(obligatory), published, deadline,
                                                     "its", "exercise", " ingen ")
                print(score)
                print("skal adde")
                DatabaseInserter.add_user_completed_assignment(username, course_code, i + 1, "exercise", score)
                print("Har addet.")

                driver.back()
                driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
                link = driver.find_elements_by_class_name("GridTitle")
            except:
                print("\nNot an supported assignment\n")
                driver.back()
                driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
                link = driver.find_elements_by_class_name("GridTitle")


    # TODO: This code works for Programvareutvikling, needs further testing.
    def get_all_assignments(self):

        for i in range(0, len(self.get_course_list())):
            self.get_assignments(i)


    def get_announcements(self):
        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")


        # TODO: This code works for Programvareutvikling, needs further testing.
        # Navigates to the first course
        print("Getting messages from: " + courses[1].text[0:7]+"\n")
        courses[1].click()
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        announcements = driver.find_elements_by_class_name("h-ov-hidden")
        announcer = driver.find_elements_by_class_name("h-va-bottom")

        # print(len(announcements))
        # print(announcements[0].text)

        for i in range(0, len(announcements)):
            print(announcer[i].text+":")
            print(announcements[i].text)
            print("")

    def close_driver(self):
        driver.quit()


username = "marihl"
password = input("Password: ")

myScraper = tempScraper(username, password)
myScraper.get_course_list()
myScraper.get_assignments(3)



myScraper.close_driver()
