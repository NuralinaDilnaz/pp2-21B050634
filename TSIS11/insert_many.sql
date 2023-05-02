DROP TABLE IF EXISTS PHONEBOOK;
CREATE TABLE PHONEBOOK (
	id SERIAL PRIMARY KEY,
    account_name VARCHAR(20) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(50) NOT NULL
);
INSERT INTO
   PHONEBOOK
VALUES
('1', 'Aika', '8 123 456 78 90', 'Aktobe'),
('2', 'Elina', '8 456 234 67 45', 'Astana'),
('3', 'Aiganym', '8 707 345 46 88', 'Shymkent'),
('4', 'Amina', '8 747 555 45 45', 'Almaty');
SELECT * FROM PHONEBOOK

