-- CREATE TABLE purchases(
-- id_purchases SERIAL PRIMARY KEY,
-- customer_id INTEGER NOT NULL,
-- item_id INTEGER NOT NULL,
-- quantity_purchased INTEGER NOT NULL,

-- FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
-- FOREIGN KEY (item_id) REFERENCES items(items_id)
-- );


-- select * from purchases;
-- SELECT  * FROM items;
-- SELECT * FROM customers;

-- SELECT id_purchases, customer_id, item_id, quantity_purchased;
-- INSERT INTO purchases(customer_id, item_id, quantity_purchased)
-- VALUES 
-- (select * FROM customers s WHERE s.customer_id = 3, 2, 10);

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- SELECT c.customer_id, i.items_id, 1
-- FROM customers c
-- JOIN items as i ON i.items_id = 3
-- WHERE c.first_name = 'Scott' AND c.last_name = 'Scott';

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- SELECT c.customer_id, i.items_id, 10
-- FROM customers as c
-- JOIN items as i ON i.items_id = 2
-- WHERE c.first_name = 'Melanie' AND c.last_name = 'Johnson';

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- SELECT c.customer_id, i.items_id, 2
-- FROM customers as c
-- JOIN items as i ON i.items_id = 1
-- WHERE c.first_name = 'Gerg' AND c.last_name = 'Jones';

-- SELECT * FROM purchases as p 
-- JOIN customers as s ON p.customer_id = s.customer_id;

-- SELECT * FROM purchases as p 
-- JOIN items as s ON p.customer_id = s.items_id;

-- SELECT customer_id, first_name, last_name, items_size, price
-- FROM customers as c
-- JOIN items as i ON i.items_id = 1
-- WHERE c.customer_id = 5;

-- SELECT customer_id, first_name, last_name, items_size, price
-- FROM customers as c
-- JOIN items as i ON i.items_id = 1
-- WHERE i.items_id = 2 OR i.items_id = 1;

-- SELECT first_name, last_name, items_size FROM customers as s 
-- JOIN items as i ON s.customer_id = i.items_id;

