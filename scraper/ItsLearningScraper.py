from selenium import webdriver
import os
import platform
from database import DatabaseInserter
import timestring

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
driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning


class ItsLearningScraper:
    def __init__(self, username, password):

        self.username = username
        self.password = password

        # logs into Its Learning. After this the "driver" contains the main page in Its Learning
        username_field = driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()

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

        # clicks the "abonner" button
        cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_ctl03_SubscribeLink")
        cal.click()

        # extracts the calendar feed url and returns it as a string
        webcal_url = driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink").text

        # creates a ical-version of the feed to make it compatible with the icalendar library.
        ical_url = webcal_url.replace("webcal", "https")

        # This URL structure can be used to subscribe to a calendar by URL, implement feature if necessary
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics

        DatabaseInserter.add_itslearning_url(ical_url)

    # returns the user course list as a list of strings
    def get_course_list(self):

        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

        course_list = []

        for course in courses:
            # '.text' extracts the text contained in the WebElement (which is what Selenium extracts)
            course_list.append(course.text.split()[0])
            DatabaseInserter.add_user_has_course(self.username, str(course.text.split()[0]))

        return course_list

    # Should be splitted into several methods, but have not found a robust solution that Selenium supports yet.
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

        # Trying to find a folder containing assignments
        try:
            link = driver.find_element_by_link_text("Assignments")
        except:
            try:
                link = driver.find_element_by_link_text("Øvinger")
            except:
                return "Unable to find assignments for " + course_code

        link.click()
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        link = driver.find_elements_by_class_name("GridTitle")

        # loops through every element in the assignment folder, tries to extract info
        for i in range(0, len(link)):
            link[i].click()

            try:
                title = driver.find_elements_by_class_name("ccl-pageheader-title")[0].text
                attribute = driver.find_elements_by_class_name("h-mrb5")

                published = attribute[0].text[11:]
                deadline = attribute[1].text.replace("Deadline: ", "")
                deadline = str(datetime_converter(deadline))

                if "Ja" in attribute[2].text:
                    obligatory = True
                else:
                    obligatory = False

                if "Ja" in attribute[3].text:
                    anonymous = True
                else:
                    anonymous = False

                print("Title: " + title)
                print("Published: " + published)
                print("Deadline: " + deadline)
                print("Obligatory: " + str(obligatory))
                print("Anonym: " + str(anonymous))

                try:
                    assessment = driver.find_element_by_class_name("colorbox_green").text
                except:
                    assessment = None
                print("Assessment: " + assessment)

                if "Godkjent/Vurdert" in assessment:
                    score = 1
                else:
                    score = 0
                print("Score: " + score)

                try:
                    DatabaseInserter.add_assignment_data(course_code, title, i + 1, str(obligatory), published, deadline,
                                                     "its", "exercise", " ingen ")
                    DatabaseInserter.add_user_completed_assignment(self.username, course_code, i + 1, "exercise", score)
                except:
                    print("Daabase Error")

                driver.back()

                driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

                link = driver.find_elements_by_class_name("GridTitle")

            except:
                print("\nNot an supported assignment\n")
                driver.back()
                driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
                link = driver.find_elements_by_class_name("GridTitle")

    def get_all_assignments(self):
        for i in range(0, len(self.get_course_list())):
            self.get_assignments(i)


    def get_announcements(self, index):
        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

        # Navigates to the first course
        print("Getting messages from: " + courses[index].text.split()[0]+"\n")
        courses[index].click()
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


def datetime_converter(datestring):
    print(datestring)
    split = datestring.split()
    inp = translate(split[1]) + " " + split[0][0:2] + " " + split[2] + split[3]
    dt = timestring.Date(inp)

    return dt


def translate(month):
    if month == "januar":
        return "january"
    elif month == "februar":
        return "february"
    elif month == "mars":
        return "march"
    elif month == "april":
        return "april"
    elif month == "mai":
        return "may"
    elif month == "juni":
        return "june"
    elif month == "juli":
        return "july"
    elif month == "oktober":
        return "october"
    elif month == "desember":
        return "december"
    else:
        return month

"""

username = "evenkal"
password = input("Password: ")

scraper = ItsLearningScraper(username, password)

try:
    scraper.get_all_assignments()
except:
    print("Fail")

scraper.close_driver()


"""
