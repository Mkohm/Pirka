from selenium import webdriver
import os
import platform
from database import DatabaseInserter
import timestring


class ItsLearningScraper:

    def __init__(self, username: str, password: str):
        """
        This method sets up scraper, and logs in to Its Learning. It enables the other methods to scrap
        content, like calendar feed, exercises and course list.
        :param username: FEIDE-username
        :param password: FEIDE-password
        """

        self.username = username
        self.password = password

        # Initializes the correct version of chromedriver with regards to OS
        driver_directory = os.path.dirname(__file__)
        if platform.system() == "Windows":
            relative_path = "chromedriver.exe"
        else:
            relative_path = "chromedriver"
        absolute_file_path = os.path.join(driver_directory, relative_path)
        chrome_profile = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=absolute_file_path)

        self.driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning

        # logs into Its Learning. After this the "driver" contains the main page in Its Learning
        username_field = self.driver.find_element_by_name("feidename")
        username_field.send_keys(username)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()

    def get_calendar_feed(self):
        """
        This method extracts the personalized calendar feed for a user, and stores it in the database.
        """
        # navigates to the calendar page in Its Learning.
        self.driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Calendar%2fSchedule.aspx&Item=l-menu-calendar")

        # navigates to the body frame to be able to navigate further
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))

        # expand the menu button (with three dots) above the calender, on the right side of the page
        cal = self.driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_PageFunctions")
        cal.click()

        # clicks the "abonner" button
        cal = self.driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_ctl03_SubscribeLink")
        cal.click()

        # extracts the calendar feed url and returns it as a string
        webcal_url = self.driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink").text

        # creates a ical-version of the feed to make it compatible with the icalendar library.
        ical_url = webcal_url.replace("webcal", "https")

        # This URL structure can be used to subscribe to a calendar by URL, implement feature if necessary in future
        # https://www.google.com/calendar/render?cid=http://www.example.com/calendar.ics

        DatabaseInserter.add_itslearning_url(ical_url)


    def get_course_list(self):
        """
        This method scrapes Its Learning to get all the users active courses, and then
        stores it in the database.
        :return: course_list, a list of all the users active courses in Its Learning.
        """
        # gets the course overview page
        self.driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = self.driver.find_elements_by_css_selector("td > .ccl-iconlink")

        course_list = []
        for course in courses:
            # '.text' extracts the text contained in the WebElement (which is what Selenium extracts)
            course_list.append(course.text.split()[0])
            DatabaseInserter.add_user_has_course(self.username, str(course.text.split()[0]))

        return course_list

    # Should be splited into several methods, but have not found a robust solution that Selenium supports yet.
    def get_assignments(self, course_index):
        """
        Iterates through all assignments for the course placed at index 'course_index' in the
        users course list in Its Learning
        :param course_index: Index of the course the assignment is scraped from.
        :return:
        """


        # gets the course overview page
        self.driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = self.driver.find_elements_by_css_selector("td > .ccl-iconlink")

        # Navigates to the relevant course based in course index
        course_code = courses[course_index].text.split()[0]
        # TODO: REMOVE
        print("Extracting info from: " + course_code)
        courses[course_index].click()

        # Trying to find a folder containing assignments. Only assignment located directly below a top level folder
        # in Its Learning's folder structure.
        try:
            link = self.driver.find_element_by_link_text("Assignments")
        except:
            try:
                link = self.driver.find_element_by_link_text("Øvinger")
            except:
                return "Unable to find assignments for " + course_code

        # Navigates inside the assignment folder
        link.click()
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))
        link = self.driver.find_elements_by_class_name("GridTitle")

        # loops through every element in the assignment folder, tries to extract info
        for i in range(0, len(link)):
            link[i].click()

            try:
                title = self.driver.find_elements_by_class_name("ccl-pageheader-title")[0].text
                attribute = self.driver.find_elements_by_class_name("h-mrb5")

                published = attribute[0].text[11:]
                deadline = attribute[1].text.replace("Deadline: ", "")
                deadline = str(datetime_converter(deadline))

                if "Ja" in attribute[2].text:
                    obligatory = 1
                else:
                    obligatory = 0

                if "Ja" in attribute[3].text:
                    anonymous = True
                else:
                    anonymous = False

                # TODO: REMOVE
                print("Title: " + title)
                print("Published: " + published)
                print("Deadline: " + deadline)
                print("Obligatory: " + str(obligatory))
                print("Anonym: " + str(anonymous))

                try:
                    assessment = self.driver.find_element_by_class_name("colorbox_green").text
                    print("Assessment: " + assessment)
                except:
                    assessment = "None"
                    print("Assessment: none")

                # print("test")
                # if "Godkjent/Vurdert" == assessment:
                #     score = 1
                #     print("Score: " + score)
                # else:
                #     score = 0
                #     print("Score: " + score)
                #
                # print("test111")

                score = 1

                try:
                    DatabaseInserter.add_assignment_data(course_code, title, i + 1, str(obligatory), published, deadline,
                                                     "its", "exercise", " ingen ")
                except:
                    print("Database Error1")
                try:
                    DatabaseInserter.add_user_completed_assignment(self.username, course_code, i + 1, "exercise", score)
                except:
                    print("Database Error2")


                # makes the driver ready for a new iteration of the loop
                self.driver.back()
                self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))
                link = self.driver.find_elements_by_class_name("GridTitle")

            except:
                print("\nNot an supported assignment\n")
                self.driver.back()
                self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))
                link = self.driver.find_elements_by_class_name("GridTitle")

    def get_all_assignments(self):
        for i in range(0, len(self.get_course_list())):
            self.get_assignments(i)


    def get_announcements(self, index):
        # gets the course overview page
        self.driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = self.driver.find_elements_by_css_selector("td > .ccl-iconlink")

        # Navigates to the first course
        print("Getting messages from: " + courses[index].text.split()[0]+"\n")
        courses[index].click()
        self.driver.switch_to.frame(self.driver.find_element_by_name("mainmenu"))
        announcements = self.driver.find_elements_by_class_name("h-ov-hidden")
        announcer = self.driver.find_elements_by_class_name("h-va-bottom")

        # print(len(announcements))
        # print(announcements[0].text)

        for i in range(0, len(announcements)):
            print(announcer[i].text+":")
            print(announcements[i].text)
            print("")

    def close_driver(self):
        self.driver.quit()


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






