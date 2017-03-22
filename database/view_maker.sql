Create view status_exercise(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_exercise from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='exercise'
GROUP BY U.course_code, U.username;

Create view status_project(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_project from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='project'
GROUP BY U.course_code, U.username;

Create view status_lab(username, course_code, total_score, req_score) as select U.username, U.course_code, sum(U.score),
C.req_lab from user_has_assignment as U, course as C where U.course_code = C.course_code and U.category='lab'
GROUP BY U.course_code, U.username;


Select S.username, S.total_score, S.req_score, C.course_name from status_exercise as S,
  course as C where S.course ="tdt4100" and S.course = C.course_code and S.username = "marihl" group by
  S.username ;