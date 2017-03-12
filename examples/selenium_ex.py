
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import urllib3
import icalendar
import getpass


# TODO: This has only been used for exprimenting so far. Create a proper code structure and documentation

# il_username = input("NTNU username: ")
# il_password = getpass.getpass("NTNU password: ", stream=None) # Function for hiding password input

def init_driver():
    global driver
    chrome_profile = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chrome_profile)



def scrape():
    # Log in via Feide
    driver.get("http://www.ilearn.sexy") # Shortcut to itslearning
    username = driver.find_element_by_name("feidename")
    username.send_keys("evenkal") # TODO: add your own user name if you want to test
    password = driver.find_element_by_name("password")
    password.send_keys("roPstAd1337CC4l") # TODO: add your own password if you want to test
    password.submit()

    # Go to course list
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_id('l-header')) # Wait for the site to load properly
    # driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx") # Go to course list
    # driver.switch_to.frame(driver.find_element_by_name("mainmenu")) # itslearning uses iframes, let's go to the corrct one


    driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Calendar%2fSchedule.aspx&Item=l-menu-calendar")
    driver.switch_to.frame(driver.find_element_by_name("mainmenu")) # itslearning uses iframes, let's go to the corrct one
    cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_PageFunctions")

    cal.click()

    cal = driver.find_element_by_id("ctl00_PageFunctionsPlaceHolder_ctl03_SubscribeLink")

    cal.click()

    lenk = driver.find_element_by_id("ctl00_ContentPlaceHolder_ICalFeedModalDialog_ICalFeedLink")
    print(lenk.text)


    req = urllib3.Request(lenk.text)
    response = urllib3.urlopen(req)
    data = response.read()

    cal = Calendar.from_ical(data)

    for event in cal.walk('vevent'):

        start = event.get('dtstart')
        summery = event.get('summary')

        print(start.dt)
        print(str(summery))


    # cal = driver.find_element_by_link_text("/main.aspx?TextURL=Calendar%2fSchedule.aspx&Item=l-menu-calendar")
    # cal.click()



    # # Fetch and print courses
    # courses = driver.find_elements_by_css_selector("td > .ccl-iconlink") # "ccl-iconlink" is the classname associated with hyperlinks. For courses, these are children of the "td" tag
    #
    #
    #
    #
    # course = courses[0]
    #
    # courses[1].click()
    #
    # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
    #
    # task_table = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder_DashboardLayout']/div[2]/ul/li[2]")
    #
    # print(task_table)
    #
    # tasks = task_table.find_elements_by_class_name("h-va-baseline")
    #
    #
    #
    #
    # for task in tasks:
    #     task.click()
    #     driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
    #     task_title = driver.find_elements_by_class_name("ccl-pageheader")
    #     print(task_title[0].text)
    #     date = driver.find_elements_by_class_name("h-mrb5")
    #     print(date[1].text)
    #     driver.back()
    #     print("Back")


    # tasks[0].click()
    #
    # driver.switch_to.frame(driver.find_element_by_name("mainmenu"))
    # task_title = driver.find_elements_by_class_name("ccl-pageheader")
    # print(task_title[0].text)
    # date = driver.find_elements_by_class_name("h-mrb5")
    # print(date[1].text)

if __name__ == "__main__":
    init_driver()
    scrape()
