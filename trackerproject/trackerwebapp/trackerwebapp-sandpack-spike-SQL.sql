-- SQLite
DELETE from trackerwebapp_student;
DELETE from trackerwebapp_studentcohort;
Delete from trackerwebapp_cohort;
Delete from trackerwebapp_exercise;
Delete from trackerwebapp_language;
Delete from trackerwebapp_submission;

-- create students
INSERT into trackerwebapp_student ('first_name', 'last_name')
Values ("Bubba", "Sparkle");

INSERT into trackerwebapp_student ('first_name', 'last_name')
Values ("Fred", "Jones");


-- create cohorts
INSERT into trackerwebapp_cohort
Values (null, "C56");

-- create cohort students
INSERT into trackerwebapp_studentcohort
Values (null, null, null, 5, 9);

INSERT into trackerwebapp_studentcohort
Values (null, null, null, 5, 10);

-- create languages
INSERT into trackerwebapp_language
VALUES (null, "JavaScript");

-- create exercises
INSERT into trackerwebapp_exercise
VALUES (null, "Functions That Give Back", 4);

-- SELECTS
SELECT * from trackerwebapp_student;
SELECT * from trackerwebapp_cohort;
SELECT * from trackerwebapp_studentcohort;
select * from trackerwebapp_student where last_name like 'Sparkle';
select * from trackerwebapp_language;
select * from trackerwebapp_exercise;
select * from trackerwebapp_submission;





