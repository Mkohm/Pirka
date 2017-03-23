from selenium import webdriver
import os
import platform

def login(username, password):
    driver_directory = os.path.dirname(__file__)
    if (platform.system() == "Windows"):
        relative_path = "chromedriver.exe"
    else:
        relative_path = "chromedriver"
    absolute_file_path = os.path.join(driver_directory, relative_path)
    driver = webdriver.Chrome(executable_path=absolute_file_path)
    driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning

    username_field = driver.find_element_by_name("feidename")
    username_field.send_keys(username)
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)
    password_field.submit()
    driver.close()


def get_course_list(username, password):
    driver_directory = os.path.dirname(__file__)
    if (platform.system() == "Windows"):
        relative_path = "chromedriver.exe"
    else:
        relative_path = "chromedriver"
    absolute_file_path = os.path.join(driver_directory, relative_path)

    driver = webdriver.Chrome(executable_path=absolute_file_path)
    driver.get("http://www.ilearn.sexy")  # Shortcut to itslearning

    username_field = driver.find_element_by_name("feidename")
    username_field.send_keys(username)
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)
    password_field.submit()

    # gets the course overveiw page
    driver.get("https://ntnu.itslearning.com/main.aspx?TextURL=Course%2fAllCourses.aspx")
    driver.switch_to.frame(driver.find_element_by_name("mainmenu"))

    # finds all the hyperlinks in the frame. They are all named "ccl-iconlink" in HTML
    courses = driver.find_elements_by_css_selector("td > .ccl-iconlink")

    course_list = []

    for course in courses:
        # '.text' extracts the text contained in the WebElement (which is what Selenium extracts)
        course_list.append(course.text.split()[0])

    driver.quit()

    return course_list
