CREATE DATABASE IF NOT EXISTS notes_app_v2;
USE notes_app_v2;

CREATE TABLE users(
    id INT(25) NOT NULL AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL,
    last_name VARCHAR(70) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    CONSTRAINT PK_users PRIMARY KEY(id),
    CONSTRAINT UC_email UNIQUE(email)
)ENGINE=InnoDB;

-- "ENGINE=InnoDB" means that we'll keep the "referential integrity" and all kinds of relationships 
-- between different tables.




CREATE TABLE notes(
    id INT(25) NOT NULL AUTO_INCREMENT,
    user_id INT(25) NOT NULL,
    title VARCHAR(50) NOT NULL,
    description MEDIUMTEXT,
    date DATE NOT NULL,
    CONSTRAINT PK_notes PRIMARY KEY(id),
    CONSTRAINT FK_user_note FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDB;

-- "MEDIUMTEXT" is a kind of tahta that allows you to store a lot of text inside




-- 1) Una vez escrito el código, compiamos y pegamos en phpmyadmin (sección SQL)
-- 2) Posteriormente ejecutamos y se crearan ambas tablas dento de la DB



