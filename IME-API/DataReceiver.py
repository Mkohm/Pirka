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

        return ("Exam date for TMA4105 is", exam_date)


    def getContactInfo(self, codeInput)-> str:
        base_url = "http://www.ime.ntnu.no/api/course/en/"

        # Fetch the course
        data = requests.get(base_url + codeInput).json()
        data2 = json.dumps(data, indent=4)
        #print(data2)

        # Get relevant data and print it
        personData = data["course"]["educationalRole"][0]["person"]

        name = personData["displayName"]
        print ()
        print ()
        print(name)
        mail = personData["email"]
        print(mail)
        office = personData["officeAddress"]
        print (office)
        phone = personData["phone"]
        print (phone)

        website_id = mail.split("@")

        base_url_ntnu = "https://www.ntnu.no/ansatte/"
        website = base_url_ntnu + website_id[0]

        print (website)

        return ("Contact info for TMA4105 is", name)






data = DataReceiver()
data.getContactInfo('TMA4100')
data.getContactInfo('TMA4130')








