INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `course_material`, `teaching_form`, `term`, 'req_exercise')
VALUES ("DUMMY2222","Dummy Intro","2017-05-31","Written examination","Marius Kohmann","kohm@ntnu.no","U1","12345678","7.5","www.kohm.ntnu.no","None","An introduction to testing Pirka","Unit testing for dummmies","Lectures","Spring", 10);

INSERT INTO `course`(`course_code`,`course_name`,`exam_date`, `assessment_form`,`contact_name`, `contact_mail`,`contact_office`,`contact_phone`,`credit`, `url`, `prereq_knowledge`, `course_content`, `course_material`, `teaching_form`, `term`, 'req_exercise')
VALUES ("DUMMY3333","Dummy Advanced","2017-05-30","Written examination","Marius Kohmann","kohm@ntnu.no","U1","12345678","7.5","www.kohm.ntnu.no","DUMMY2222 Dummy Intro","Advanced methods, Pirka bot","Practice cards intro","Lectures","Spring", 8);

INSERT INTO course_event('date_time', 'course_code', 'room', 'category') VALUES ("2017-04-30 20:15:00", "DUMMY2222", "R7", "Helping lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-03 12:15:00", "DUMMY2222", "F1", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-05 08:15:00", "DUMMY2222", "R7", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-08 18:15:00", "DUMMY2222", "EL5", "Helping Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-13 12:15:00", "DUMMY2222", "S1", "Helping lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-15 16:15:00", "DUMMY2222", "R7", "Lecture")

INSERT INTO course_eventt('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-18 14:15:00", "DUMMY2222", "R1", "Helping Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-21 20:15:00", "DUMMY2222", "R7", "Lecture")

INSERT INTO course_eventt('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-22 10:15:00", "DUMMY2222", "R7", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-29 08:15:00", "DUMMY2222", "EL3", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-01 09:15:00", "DUMMY3333", "R7", "Helping lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-04 16:15:00", "DUMMY3333", "EL5", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-07 18:15:00", "DUMMY3333", "F1", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-11 12:15:00", "DUMMY3333", "R5", "Helping lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-13 20:15:00", "DUMMY3333", "S1", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-16 08:15:00", "DUMMY3333", "R9", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-21 16:15:00", "DUMMY3333", "R7", "Helping lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-22 18:15:00", "DUMMY3333", "S2", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-25 20:15:00", "DUMMY3333", "F1", "Lecture")

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-28 10:15:00", "DUMMY3333", "EL5", "Helping lecture")

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",4,"exercise","Exercise 4", "ingen", "5. april 2017 av Kohm, Marius", "2017-04-10 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",5,"exercise","Exercise 5", "ingen", "5. april 2017 av Kohm, Marius", "2017-04-17 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",6,"exercise","Exercise 6", "ingen", "5. april 2017 av Kohm, Marius", "2017-04-24 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",7,"exercise","Exercise 7", "ingen", "5. april 2017 av Kohm, Marius", "2017-05-01 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",8,"exercise","Exercise 8", "ingen", "5. april 2017 av Kohm, Marius", "2017-05-08 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",9,"exercise","Exercise 9", "ingen", "5. april 2017 av Kohm, Marius", "2017-05-13 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",10,"exercise","Exercise 10", "ingen", "5. april 2017 av Kohm, Marius", "2017-05-20 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222", 11,"exercise","Exercise 11", "ingen", "5. april 2017 av Kohm, Marius", "2017-05-27 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",4,"exercise","Exercise 4", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-14 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",5,"exercise","Exercise 5", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-21 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",6,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-28 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",7,"exercise","Exercise 7", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-05 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",8,"exercise","Exercise 8", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-12 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",9,"exercise","Exercise 9", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-19 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",10,"exercise","Exercise 10", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-26 00:00:00","ingen",0)

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333", 11,"exercise","Exercise 11", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-06-02 00:00:00","ingen",0)