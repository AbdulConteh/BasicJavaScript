SELECT * FROM users_assignment.users;

INSERT INTO users ( first_name, last_name, email )
VALUES ( 'Bob', 'Marley', 'bob@marley.com');

SELECT * FROM users_assignment.users;

INSERT INTO users ( first_name, last_name, email )
VALUES ( 'Hulk', 'Hogan', 'hulk@hogan.com'), ( 'Jimmy', 'Hendrix', 'jimmy@hendrix.com');

SELECT * FROM users_assignment.users;

DELETE FROM users_assignment.users
 WHERE id = 5;
 
SELECT * FROM users_assignment.users;

DELETE FROM users_assignment.users
 WHERE id < 6;
 
 SELECT * FROM users_assignment.users;
 
 DELETE FROM users_assignment.users
 WHERE id > 6;
 
  SELECT * FROM users_assignment.users;
  
INSERT INTO users ( first_name, last_name, email )
VALUES ( 'Hulk', 'Hogan', 'hulk@hogan.com'), ( 'Jimmy', 'Hendrix', 'jimmy@hendrix.com'), ( 'Dwayne', 'Johnson', 'dwayne@johnson.com'), ('Elvis', 'Presley', 'elvis@presley.com' );

SELECT * FROM users_assignment.users;

SELECT * FROM users;