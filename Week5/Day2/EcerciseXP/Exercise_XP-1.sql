-- CREATE TABLE items ( 
--  id_items SERIAL PRIMARY KEY,
--  size_items VARCHAR(50),
--  price INTEGER);

-- INSERT INTO items (size_items, price) 
-- VALUES
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80);

-- SELECT * FROM items;

-- CREATE TABLE customers (
--     id_customer SERIAL PRIMARY KEY,
--     first_name VARCHAR(100),
--     last_name VARCHAR(100)
-- );

-- INSERT INTO customers(first_name, last_name)
-- VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');
-- SELECT * FROM customers;


-- SELECT * FROM items WHERE price > 80;
-- SELECT * FROM items WHERE price < 300;
-- SELECT * FROM customers WHERE last_name  = 'Smith';
-- SELECT * FROM customers WHERE last_name  = 'Jones';
-- SELECT * FROM customers WHERE first_name  != 'Scott';