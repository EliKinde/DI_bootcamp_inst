-- SELECT * FROM students;

-- CREATE TABLE students (
-- id_student SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NO NULL,
-- last_name VARCHAR(50) NO NULL,
-- birth_date DATE NO NULL
-- );

-- INSERT INTO students (first_name, last_name, birth_date)
-- VALUES 
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03');
-- SELECT * FROM students;

-- INSERT INTO students(first_name, last_name, birth_date)
-- VALUES ('Eliyho', 'kinde', '1994-05-05');
-- SELECT * FROM students;

-- SELECT first_name, last_name FROM students;
-- SELECT first_name, last_name FROM students WHERE id_student = 2;
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';
-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';

-- SELECT first_name, last_name FROM students WHERE id_student IN (1, 3);
-- SELECT * FROM students WHERE birth_date >= '01-01-2000';
