import requests
import json
class DataReceiver ():



    # TODO: Implement this
    def getExamDate(self, code) -> str:
        base_url = "http://www.ime.ntnu.no/api/course/en/"
        #code = input("Please provide a course code: ")

        # Fetch the course
        course = requests.get(base_url + code).json()

        view = json.dumps(course, indent=4)
        print(view)
        sjekk=course
        print(sjekk)

        # Get relevant data and print it
        code = course["course"]["code"]
        name = course["course"]["name"]
        exam_date = course["course"]["assessment"][0]["date"]

        print("Exam date for", code, name, "is", exam_date)




data = DataReceiver()
data.getExamDate('TDT4100')





