CREATE DATABASE library;

use library;
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(150),
    author VARCHAR(100),
    publish_year INT,
    price DECIMAL(10,2)
);
INSERT INTO books VALUES
(1, 'Python Crash Course', 'Eric Matthes', 2019, 750),
(2, 'Clean Code', 'Robert C. Martin', 2008, 950),
(3, 'The Alchemist', 'Paulo Coelho', 1988, 400),
(4, 'Atomic Habits', 'James Clear', 2018, 650),
(5, 'Introduction to Algorithms', 'Thomas H. Cormen', 2009, 1200),
(6, 'The Pragmatic Programmer', 'Andrew Hunt', 1999, 850),
(7, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 1997, 450),
(8, 'Deep Work', 'Cal Newport', 2016, 550);

SELECT * FROM books WHERE price > 500;

SELECT * FROM books order by price desc;

SELECT COUNT(*) from books as book_count;

UPDATE books SET price = 980 WHERE id = 2;