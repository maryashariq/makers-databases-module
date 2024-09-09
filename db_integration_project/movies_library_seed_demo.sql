/* The purpose of this seed SQL script is to demonstrate an understanding of the
following learning objectives:

    * Adding tables using CREATE TABLE
   * Adding entries using INSERT
   * Reading entries using SELECT
   * Updating entries using UPDATE
   * Removing entries using DELETE

This database is called movies_library, which will store movies that I have seen recently. 
The database consists of two tables - movies and directors
*/

-- CREATE DATABASE movies_library;

DROP TABLE IF EXISTS directors;
DROP SEQUENCE IF EXISTS directors_id_seq;
DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

/* 1. Adding tables using CREATE TABLE */

CREATE SEQUENCE IF NOT EXISTS directors_id_seq;
CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    country VARCHAR (255)
);

CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    release_year INTEGER,
    director_id INTEGER
);

/* 2. Adding entries using INSERT */

INSERT INTO directors (name, country) VALUES ('Luca Guadagnino', 'Italy');
INSERT INTO directors (name, country) VALUES ('Cord Jefferson', 'US');
INSERT INTO directors (name, country) VALUES ('PTA', 'US');
INSERT INTO directors (name, country) VALUES ('Santiago Mitre', 'Argentina');
INSERT INTO directors (name, country) VALUES ('Yorgos Lanthimos', 'Greece');
INSERT INTO directors (name, country) VALUES ('Alexander Payne', 'US');
INSERT INTO directors (name, country) VALUES ('Matthew Johnson', 'Canada')

INSERT INTO movies (title, release_year, director_id) VALUES ('Challengers', 2024, 1);
INSERT INTO movies (title, release_year, director_id) VALUES ('American Fiction', 2024, 2);
INSERT INTO movies (title, release_year, director_id) VALUES ('Boogie Nights', 1997, 3);
INSERT INTO movies (title, release_year, director_id) VALUES ('Argentina 1985', 2023, 4);
INSERT INTO movies (title, release_year, director_id) VALUES ('Poor Things', 2023, 5);
INSERT INTO movies (title, release_year, director_id) VALUES ('The Holdovers', 2023, 6);
INSERT INTO movies (title, release_year, director_id) VALUES ('BlackBerry', 2023, 7);
INSERT INTO movies (title, release_year, director_id) VALUES ('Licorice Pizza', 2021, 3)

/* 3. Reading entries using SELECT */
-- Get all movies released before 2024

SELECT * FROM movies WHERE release_year < 2024;
SELECT * FROM directors WHERE country = 'US'
SELECT * FROM movies WHERE release_year between 2024 and 2021

-- Get all movies from PTA

SELECT * FROM movies WHERE director_id = 3;

/* 4. Updating entries using UPDATE - first I will insert a new entry and then update it */

INSERT INTO directors (name) VALUES ('Ali Abbasi');
UPDATE directors SET country = 'Iran' WHERE name = 'Ali Abbasi';

/* 4. Removing entries using DELETE */

DELETE FROM movies WHERE title = 'American Fiction';

DELETE FROM movies WHERE year < 2024;
