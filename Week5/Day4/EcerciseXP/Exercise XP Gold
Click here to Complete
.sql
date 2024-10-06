SELECT * FROM students;

-- UPDATE students
-- SET birth_date = '1998/11/02' WHERE id_student = 3 OR id_student = 1;

-- UPDATE students SET last_name = 'Guez' WHERE id_student = 5;

-- DELETE FROM students WHERE id_student = 3;

-- SELECT COUNT(first_name) FROM students;
-- SELECT COUNT(first_name) FROM students WHERE birth_date > '2000/01/1';

-- ALTER TABLE students
-- ADD COLUMN math_grade smallint;

-- UPDATE students SET math_grade = 80 WHERE id_student = 1;
-- UPDATE students SET math_grade = 90 WHERE id_student IN (2,4);
-- UPDATE students SET math_grade = 40 WHERE id_student = 6;
-- UPDATE students SET math_grade = 75 WHERE id_student = 5;

-- SELECT COUNT(math_grade) FROM students WHERE math_grade > 83;

-- INSERT INTO students(first_name, last_name, birth_date, math_grade)
-- VALUES('Omer', 'Simpson', '1980-03-10',70);
-- SELECT * FROM students;

-- SELECT sum(math_grade) FROM students;


