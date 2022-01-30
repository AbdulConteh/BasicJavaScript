SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Mikey', 'Turtle', 23, 4), ('Ralph', 'Turtle', 19, 4), ('Leo', 'Turtle', 25, 4); 

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Might', 'Guy', 42, 5), ('Kakashi', 'Guy', 28, 5), ('Yamcha', 'Guy', 34, 5); 

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('George', 'McFly', 46, 6), ('Michael', 'McDive', 38, 6), ('Youknow', 'TheVibes', 21, 6); 

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);
    
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);


    
