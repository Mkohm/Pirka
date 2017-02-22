import requests
import json

base_url = "http://www.ime.ntnu.no/api/course/en/"
class DataReceiver ():


    @staticmethod
    def __get_data__(course_code):
        data = requests.get(base_url + course_code).json()
        return data




    def get_exam_date(self, code) -> str:

        subject = self.getData(code)


        # Get relevant data and print it
        code = subject["course"]["code"]
        name = subject["course"]["name"]
        try:
            exam_date = subject["course"]["assessment"][0]["date"]
            return "Exam date for", code, name, "is", exam_date
        except KeyError:
            return "No Exam date available"


    def getContactInfo(self, codeInput)-> str:

        # Fetch the course
        data = self.getData(codeInput)
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
        #office = personData["officeAddress"]
        #print (office)
        phone = personData["phone"]
        print (phone)

        website_id = mail.split("@")

        base_url_ntnu = "https://www.ntnu.no/ansatte/"
        website = base_url_ntnu + website_id[0]

        print (website)

        return ("Contact info for TMA4105 is", name)



    def getCourseName(self, codeInput)-> str:

        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)
        #print(data2)

        # Get relevant data and print it
        courseName = data["course"]["norwegianName"]

        print (courseName)

        return courseName

    def getCredit(self, codeInput)-> str:

        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)
        #print(data2)

        # Get relevant data and print it
        credit = data["course"]["credit"]

        print (credit)

        return credit


    def getURL(self, codeInput)-> str:

        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)
        #print(data2)

        # Get relevant data and print it
        url  = data["course"]["infoType"][0]["text"]

        print (url)

        return url

    def getFORK(self, codeInput)-> str:

        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)
        #print(data2)

        # Get relevant data and print it
        # have to fix
        fork  = data["course"]["infoType"][1]["code"]

        print (fork)

        return fork

    def getContent(self, codeInput)-> str:

        #Returns the course info in English by default.
        #Implement a Norwegian version


        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)

        # Get relevant data and print it
        content  = data["course"]["infoType"][2]["text"]

        print (content)

        return content

    def getCourseMaterial(self, codeInput) -> str:
        # Returns the course info in English by default.
        # Implement a Norwegian version


        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)

        # Get relevant data and print it
        material = data["course"]["infoType"][3]["text"]

        print(material)

        return material

    def getForm(self, codeInput) -> str:
        # Returns the course info in English by default.
        # Implement a Norwegian version


        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)

        # Get relevant data and print it
        form = data["course"]["infoType"][4]["text"]

        print(form)

        return form

    def getANBFORK(self, codeInput) -> str:
        # Returns the course info in English by default.
        # Implement a Norwegian version

        # Fetch the course
        data = self.getData(codeInput)
        data2 = json.dumps(data, indent=4)

        # Get relevant data and print it
        anbfork = data["course"]["infoType"][6]["text"]

        print(anbfork)

        return anbfork

data = DataReceiver()
data.getContactInfo('TMA4105')
data.getContactInfo('IMT5331')
print ()
data.getCourseName("TMA4130")
print()
data.getCredit("TMA4130")
print()
data.getURL("TMA4130")
print()
data.getContent("TMA4130")
print()
data.getForm("TMA4130")
print()
data.getANBFORK("TMA4130")



