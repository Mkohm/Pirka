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




