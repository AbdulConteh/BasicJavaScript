SELECT * FROM authors;

INSERT INTO authors (name)
VALUES ('Jane Austen'), ('Emily Dickinson'), ('Fyodor Dostoevsky'), ('William Shakespeare'), ('Lau Tzu');
SELECT * FROM authors;

INSERT INTO books (title, num_of_pages)
VALUES ('C Sharp', 200), ('Java', 210), ('Python', 201), ('PHP', 325), ('Ruby', 200);
SELECT * FROM books;

UPDATE books SET title = 'C#' WHERE id = 1;
SELECT * FROM books;

UPDATE authors SET name = 'Bill Shakespeare' WHERE id = 4;
SELECT * FROM authors; 

INSERT INTO favorites (author_id, book_id)
VALUES (1,1), (1,2), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3), (3,4), (3,5);
SELECT * FROM favorites;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM FAVORITES WHERE book_id = 3 AND author_id = 2;
SELECT * FROM favorites;

INSERT INTO favorites (author_id, book_id)
VALUES (5,2);
SELECT * FROM favorites;

SELECT * FROM authors
JOIN favorites ON authors.id = favorites.author_id
JOIN books ON books.id = favorites.books_id
WHERE authors.id = 3;

SELECT author_id from favorites WHERE book_id = 3 ORDER BY author_id LIMIT 1;

SELECT * FROM books 
JOIN favorites ON books.id = favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE books.id = 5;