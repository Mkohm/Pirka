-- Next event today
INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-26 12:15:00", "DUMMY2222", "F1", "Lecture");

-- Next assignment today
INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",50,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-26 12:00:00","ingen",0);

-- Todays assignments
INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",51,"exercise","Exercise 7", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-26 13:00:00","ingen",0);

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",52,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-26 23:00:00","ingen",0);

-- Tomorrows assignments
INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY3333",53,"exercise","Exercise 8", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-27 23:00:00","ingen",0);

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",54,"exercise","Exercise 9", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-27 22:30:00","ingen",0);

-- Today events
INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-26 12:15:00", "DUMMY2222", "F1", "Lecture");

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-26 14:15:00", "DUMMY2222", "F1", "Lecture");

-- Tomorrow events
INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-27 12:15:00", "DUMMY3333", "F1", "Lecture");

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-27 14:15:00", "DUMMY2222", "F1", "Lecture");


-- This weeks assignments (tests start and end)
INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",55,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-30 23:00:00","ingen",0);

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",56,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-04-24 23:00:00","ingen",0);


-- This weeks events (tests start and end)
INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-30 12:15:00", "DUMMY3333", "F1", "Lecture");

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-04-24 14:15:00", "DUMMY2222", "F1", "Lecture");


-- Next weeks assignments (tests start and end)
INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",57,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-01 23:00:00","ingen",0);

INSERT INTO assignment('course_code', 'nr', 'category', 'title', 'description', 'published', 'deadline', 'delivery_location', 'mandatory')
VALUES ("DUMMY2222",58,"exercise","Exercise 6", "ingen", "1. januar 2017 av Leonhardsen, Mari", "2017-05-07 23:00:00","ingen",0);


-- Next weeks events (tests start and end)
INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-01 12:15:00", "DUMMY3333", "F1", "Lecture");

INSERT INTO course_event('date_time', 'course_code', 'room', 'category')
VALUES ("2017-05-07 14:15:00", "DUMMY2222", "F1", "Lecture");


-- Schedule is tested by the insertions over