Create view status_exercise(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_exercise from user_completed_assignment as U, course as C where U.course_code = C.course_code and U.category='exercise'
GROUP BY U.course_code, U.username;

Create view status_project(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_project from user_completed_assignment as U, course as C where U.course_code = C.course_code and U.category='project'
GROUP BY U.course_code, U.username;

Create view status_lab(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_lab from user_completed_assignment as U, course as C where U.course_code = C.course_code and U.category='lab'
GROUP BY U.course_code, U.username;


CREATE VIEW user_event(username, course_code, date_time, category, room)
as select UHS.username, UHS.course_code, CE.date_time, CE.category, CE.room
from user_has_course as UHS, course_event as CE
where CE.course_code = UHS.course_code
group by UHS.username,CE.course_event_id

Select U.description, U.datetime, U.room, U.course_code, C.course_name from user_event order by datetime as U,
course as C where ROWNUM = 1 and U.username = "mariukoh"

CREATE VIEW user_assignment(username, course_code, deadline, category, title)
as select UHS.username, UHS.course_code, A.deadline, A.category, A.title
from user_has_course as UHS, assignment as A
where UHS.course_code = A.course_code
group by UHS.username, A.course_code, A.nr, A.title