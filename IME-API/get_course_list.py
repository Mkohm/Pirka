import requests
import json

class get_course_list():

    base_url = "http://www.ime.ntnu.no/api/course/en/"

    def get_list(self):
    subjects = requests.get().json()

    print(subjects)
    return subjects