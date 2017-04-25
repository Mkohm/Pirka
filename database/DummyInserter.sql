INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `course_material`, `teaching_form`, `term`, 'req_exercise')
VALUES ("TDT2222","Dummy Intro","2017-05-31","Written examination","Marius Kohmann","kohm@ntnu.no","U1","12345678","7.5","www.kohm.ntnu.no","None","An introduction to testing Pirka","Unit testing for dummmies","Lectures","Spring", 10);

INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `course_material`, `teaching_form`, `term`, 'req_exercise')
VALUES ("TDT3333","Dummy Advanced","2017-05-30","Written examination","Marius Kohmann","kohm@ntnu.no","U1","12345678","7.5","www.kohm.ntnu.no","TDT2222 Dummy Intro","Advanced methods, Pirka bot","Practice cards intro","Lectures","Spring", 8);

INSERT INTO course event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-07 20:15:00", "TDT2222",)