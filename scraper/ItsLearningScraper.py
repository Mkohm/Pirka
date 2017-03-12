from selenium import webdriver
import selenium.webdriver.support.ui as ui
import getpass

# TODO: When running Selenium it is necessary to close the driver. A call to self.close_driver is needed when done.

# TODO: move these varibles and make them member varibales in the class below if needed @Kohm?
chrome_profile = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_profile)
driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning

class ItsLearningScraper:
    def __init__(self):

        # TODO: add functionality for user credentials as parameters, not hardcoded like it is now
        # Hardcoding is only for testing purposes.

        # self.username = username
        # self.password = password

        # logs into Its Learning. After this the "driver" contains the main page in Its Learning
        username = driver.find_element_by_name("feidename")
        username.send_keys("HER MÅ DU LEGGE INN BRUKERNAVN") # TODO: add your own user name if you want to test
        password = driver.find_element_by_name("password")
        password.send_keys("HER MÅ DU LEGGE INN PASSORD") # TODO: add your own password if you want to test
        password.submit()


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

        return driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink").text

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
        courses[1].click()

        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
        print(task_table.text)

        tasks = task_table.find_elements_by_class_name("h-va-baseline")


        for i in range(0, len(tasks)):
            tasks[i].click()
            driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
            date = driver.find_elements_by_class_name("itsl-detailed-info")
            print(date)
            driver.back()
            driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
            task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
            tasks = task_table.find_elements_by_class_name("h-va-baseline")


    def get_completed_assignments(self):
        # gets the course overview page
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
        courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")


        # TODO: This code works for Programvareutvikling, needs further testing.
        # Navigates to the first course
        courses[0].click()

        driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

        task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
        print(task_table.text)

        # TODO: Work in progress

        #completed_tasks = task_table.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder_DashboardLayout']/div[2]/ul/li[2]/div[2]/div[1]/ul/li[2]/a")

        # completed_task = driver.find_elements_by_css_selector("ccl-iconlink")
        #
        # task = completed_task[0]
        # task.click()

        # completed_tasks.click()
        # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
        # task_table = driver.find_element_by_css_selector("li.il-widget.itsl-cb-tasks")
        # print(task_table.text)


    def close_driver(self):
        driver.quit()

myScrape = ItsLearningScraper()

# print(myScrape.get_course_list())
# print(myScrape.get_calendar_feed())

# myScrape.get_assignments()

myScrape.get_completed_assignments()

myScrape.close_driver()

