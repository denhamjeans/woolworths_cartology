-----------------------------------------------------------------------------------------------------
-- 1. Write a query which shows the rank of student for each subject.
SELECT subject, student_id, score, DENSE_RANK() OVER (PARTITION BY subject ORDER BY score DESC) as subject_rank
     FROM students
     ORDER BY subject;


-----------------------------------------------------------------------------------------------------
-- 2. Find the Score of the students for Subject A whose average score across all subjects
-- are greater than 70.

-- SELECT student_id, AVG(score)
-- FROM students
-- GROUP BY student_id;

-- There will be none returned as none have an average score accross all subjects > 70.
-- In practice it might be worth clarifying if it is important that the students have an average score > 70 across all the available subjects,
-- or only an average score > 70 for the subjects where the student has a recorded score.

-- FUll solution to return this result
WITH cte AS (SELECT student_id, AVG(score) AS avg_score
             FROM students
             GROUP BY student_id)

SELECT s.student_id, s.score
FROM students s
INNER JOIN cte ON s.student_id = cte.student_id 
WHERE cte.avg_score > 70
    AND s.subject = 'A';


-----------------------------------------------------------------------------------------------------
-- 3. Write a query to find out the subjects which were taken by only one student and show
-- the student ID and Score for those subjects.
SELECT MAX(student_id), MAX(score), subject
FROM students
GROUP BY subject
HAVING COUNT(student_id) = 1



-- Alternative solution:

-- WITH cte AS (SELECT subject
--              FROM students
--              GROUP BY subject
--              HAVING count(student_id) = 1)

-- SELECT s.subject, s.student_id, s.score
-- FROM students s, cte
-- WHERE s.subject = cte.subject;