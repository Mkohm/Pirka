
@staticmethod
def add_exam_date():
    # Fetch the course
    data = get_data()
    name = get_course_name()

    try:
        exam_date = data["course"]["assessment"][0]["date"]
        exam_date_string = format_date(exam_date)
        exam_date = "Exam date for " + str(course_code) + " " + str(name) + " is " + str(exam_date_string)
    except KeyError:
        set_is_active_course()
        get_assessment_form()

        if not course_active:
            exam_date = "No exam date available because the course is not active."
        elif assessment_form != "Written examination":
            exam_date = "No exam date available because assessment form is: " + assessment_form
        else:
            exam_date = "No exam date available"
