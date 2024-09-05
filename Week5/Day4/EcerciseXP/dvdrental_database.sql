-- SELECT * FROM customer;

-- SELECT (first_name || ' ' || last_name) AS full_name FROM customer;

-- SELECT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film;

-- SELECT address, phone FROM address WHERE district = 'Texas';

-- SELECT * FROM film WHERE film_id = 15 or film_id = 50;

-- SELECT film_id, title, description, length,rental_rate FROM film WHERE 'Baked Cleopatra' = title;

-- SELECT film_id, title, description, length,rental_rate FROM film WHERE title LIKE 'Ba%';

-- SELECT amount FROM payment WHERE amount > 0 ORDER BY amount ASC LIMIT 10;

-- SELECT amount FROM payment ORDER BY amount ASC OFFSET 20 ROWS FETCH FIRST 10 ROW ONLY;

-- SELECT city, country FROM city INNER JOIN country;

-- SELECT city, country FROM city JOIN country ON country.country_id = city.country_id;

-- SELECT first_name, last_name, amount FROM customer JOIN payment ON customer.customer_id = payment.customer_id;

-- SELECT title FROM inventory JOIN film ON film.film_id != inventory.film_id;