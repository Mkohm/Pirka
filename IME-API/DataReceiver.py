import requests
import json
class DataReceiver ():



    # TODO: Implement this
    def getExamDate(self, code) -> str:
        base_url = "http://www.ime.ntnu.no/api/course/en/"

        # Fetch the course
        subject = requests.get(base_url + code).json()




        # Get relevant data and print it
        code = subject["course"]["code"]
        name = subject["course"]["name"]

        try:
                exam_date = subject["course"]["assessment"][0]["date"]
                return ("Exam date for", code, name, "is", exam_date)


        except KeyError:
                return("No exam date available")






