Create view status_exercise(username, course, totalScore, reqScore) as select U.username, U.course_code, sum(U.score),
C.req_exercise from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='exercise'
GROUP BY U.course_code, U.username;

Create view status_project(username, course, totalScore, reqScore) as select U.username, U.course_code, sum(U.score),
C.req_project from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='project'
GROUP BY U.course_code, U.username;

Create view status_lab(username, course, totalScore, reqScore) as select U.username, U.course_code, sum(U.score),
C.req_lab from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='lab'
GROUP BY U.course_code, U.username;