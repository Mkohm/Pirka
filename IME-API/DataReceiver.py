import requests
import json
class DataReceiver ():



    # TODO: Implement this
    def getExamDate(self, codeInput) -> str:


        base_url = "http://www.ime.ntnu.no/api/course/en/"

        # Fetch the course
        course = requests.get(base_url + codeInput).json()
        course2 = json.dumps(course, indent=4)
        print(course2)
        print(course2)
        #code = input("Please provide a course code: ")

        # Get relevant data and print it
        exam_date = course["course"]["assessment"][0]["date"]

        print(exam_date + " test")

        return ("Exam date for", code, name, "is", exam_date)

data = DataReceiver()
data.getExamDate('TDT4140')





