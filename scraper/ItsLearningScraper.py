from selenium import webdriver
import selenium.webdriver.support.ui as ui
# DOCUMENTATION: http://selenium-python.readthedocs.io/locating-elements.html

# TODO: When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these varibles and make them member varibales in the class below if needed @Kohm?


chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="/Users/mariuskohmann/PycharmProjects/Pirka/examples/chromedriver")
driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning



class ItsLearningScraper:
    def __init__(self, username, password):

        # TODO: add functionality for user credentials as parameters, not hardcoded like it is now
        # Hardcoding is only for testing purposes.

        # self.username = username
        # self.password = password

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


        return course_list

    def get_assignments(self):

        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")


        # TODO: This code works for Programvareutvikling, needs further testing.
        # Navigates to the first course
        # courses[0].click()
        #
        # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        #
        # task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
        #
        # print(task_table)
        #
        # tasks = task_table.find_elements_by_class_name("h-va-baseline")
        #
        # tasks[0].click()
        # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        # task_title = driver.find_elements_by_class_name("ccl-pageheader")
        # print(task_title[0].text)
        # date = driver.find_elements_by_class_name("h-mrb5")
        # print(date[1].text)
        # driver.back()

        # TODO: Having trouble with extracting the deadline for Itslearning quizzes. Must fix.
        # Navigates to the second course. For me this is KTN where I have only have quizzes, and not regular
        # hand ins. This causes some trouble.



        courses[0].click()

        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
        # print(task_table.text)

        tasks = task_table.find_elements_by_class_name("h-va-baseline")

        for i in range(0, len(tasks)):
            tasks[i].click()
            driver.implicitly_wait(5)
            driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
            date = driver.find_elements_by_class_name("itsl-detailed-info")
            print(date)
            driver.back()
            driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
            task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
            tasks = task_table.find_elements_by_class_name("h-va-baseline")

    # TODO: This code works for Programvareutvikling, needs further testing.
    def get_all_assignments(self):
        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

        # Navigates to the first course
        courses[0].click()


        # TODO: Implement support for different link text like "Øving"
        link = driver.find_element_by_link_text("Assignments")
        link.click()

        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        link = driver.find_elements_by_class_name("GridTitle")

        for i in range(0, len(link)):
            link[i].click()
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
            assessment = driver.find_element_by_class_name("colorbox_green").text

            print("Title: " + title)
            print("Published: " + published)
            print("Deadline: " + deadline)
            print("Obligatory: " + str(obligatory))
            print("Anonym: " + str(anonymous))
            print("Group: " + group)
            print("Assessment: " + assessment)
            print(" ")


            driver.back()
            driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
            link = driver.find_elements_by_class_name("GridTitle")


    def get_announcements(self):
        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")


        # TODO: This code works for Programvareutvikling, needs further testing.
        # Navigates to the first course
        courses[0].click()
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        announcements = driver.find_elements_by_class_name("h-ov-hidden")
        announcer = driver.find_elements_by_class_name("h-va-bottom")

        # print(len(announcements))
        # print(announcements[0].text)

        for i in range(0, len(announcements)):
            print(announcer[i].text+":")
            print(announcements[i].text)
            print("")


        #
        # for guy in announcer:
        #     print(guy.text)
        #
        # for news in announcements:
        #     print(news.text)



    def close_driver(self):
        driver.quit()
