# Selenium Web Scraping Example
# This example shows how to log in to itslearning and fetch a user's course list
# Author: Audun Liberg

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from getpass import getpass

il_username = input("NTNU username: ")
il_password = getpass("NTNU password: ") # Function for hiding password input

def init_driver():
    global driver
    chrome_profile = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chrome_profile)

def scrape():
    # Log in via Feide
    driver.get("http://www.ilearn.sexy") # Shortcut to itslearning
    username = driver.find_element_by_name("feidename")
    username.send_keys(il_username)
    password = driver.find_element_by_name("password")
    password.send_keys(il_password)
    password.submit()

    # Go to course list
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_id('l-header')) # Wait for the site to load properly
    driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx") # Go to course list
    driver.switch_to.frame(driver.find_element_by_name("mainmenu")) # itslearning uses iframes, let's go to the corrct one

    # Fetch and print courses
    courses = driver.find_elements_by_css_selector("td > .ccl-iconlink") # "ccl-iconlink" is the classname associated with hyperlinks. For courses, these are children of the "td" tag
    for course in courses:
        print(course.text)

if __name__ == "__main__":
    init_driver()
    scrape()
