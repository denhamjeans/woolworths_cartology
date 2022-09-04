CREATE TABLE students (student_id INTEGER, subject TEXT, score INTEGER);

INSERT INTO students (student_id, subject, score) VALUES (1,"A",60);
INSERT INTO students (student_id, subject, score) VALUES (1,"B",70);
INSERT INTO students (student_id, subject, score) VALUES (1,"C",40);
INSERT INTO students (student_id, subject, score) VALUES (2,"B",30);
INSERT INTO students (student_id, subject, score) VALUES (2,"C",50);
INSERT INTO students (student_id, subject, score) VALUES (2,"E",70);
INSERT INTO students (student_id, subject, score) VALUES (3,"C",30);
INSERT INTO students (student_id, subject, score) VALUES (3,"D",90);
INSERT INTO students (student_id, subject, score) VALUES (3,"F",45);

SELECT * FROM students;