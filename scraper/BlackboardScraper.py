from selenium import webdriver
import selenium.webdriver.support.ui as ui
from getpass import getpass


class BlackboardScraper:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        chrome_profile = webdriver.ChromeOptions()
        driver = webdriver.Chrome("/Users/mariuskohmann/PycharmProjects/Pirka/examples/chromedriver")

        driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning
        username = driver.find_element_by_name("feidename")
        username.send_keys(self.username)
        password = driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.submit()

        # Go to course list
        wait = ui.WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.find_element_by_id('l-header'))  # Wait for the site to load properly
        driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")  # Go to course list
        driver.switch_to.frame(
            driver.find_element_by_name("mainmenu"))  # itslearning uses iframes, let's go to the corrct one

        # Fetch and print courses
        courses = driver.find_elements_by_css_selector(
            "td > .ccl-iconlink")  # "ccl-iconlink" is the classname associated with hyperlinks. For courses, these are children of the "td" tag
        for course in courses:
            print(course.text)


    def is_valid_login_details(self):
        #Try to login
        pass




