-- SELECT * FROM language;
-- SELECT * FROM film;

-- SELECT title, description, language FROM film
-- JOIN language ON film.language_id = language.language_id;

-- SELECT title, description, name FROM language
-- LEFT JOIN film ON film.language_id = language.language_id;

-- CREATE TABLE new_film(
-- film_id SERIAL PRIMARY KEY,
--  name VARCHAR(50) NOT NULL
--  );

-- INSERT INTO new_film(name)
-- VALUES 
-- ('The Avater'),
-- ('The Avengers'),
-- ('Bad boyes');
-- select * from new_film;

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT NOT NULL,
--     language_id INT NOT NULL,
--     title VARCHAR(255) NOT NULL,
--     score INT NOT NULL CHECK (score BETWEEN 1 AND 10),
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (film_id) REFERENCES new_film(film_id) ON DELETE CASCADE,
--     FOREIGN KEY (language_id) REFERENCES language(language_id)
-- );

-- select * from language;
-- select * from customer_review;
-- INSERT INTO customer_review(film_id, language_id, title, score, review_text)
-- VALUES(1, 1, 'A Great Movie', 8, 'the first great a movies is see'),
-- (2,1,'Awsome movei', 9, 'The Heros saves the dayas'),
-- (3,1,'a avrger moive', 6, 'not bad movies not mouch about the movie');

-- DELETE FROM new_film WHERE name = 'The Avater';

-- select film_id,title,name from film INNER JOIN language ON film.language_id=language.language_id WHERE film.language_id != 1;

-- UPDATE film
-- SET language_id = 3 WHERE film_id = 1;

