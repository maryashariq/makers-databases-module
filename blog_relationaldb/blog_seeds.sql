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

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

/* 1. Adding tables using CREATE TABLE */

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  username text,
  comment_content text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);


/* 2. Adding entries using INSERT */

INSERT INTO posts (title, post_content) VALUES ('My First Post', 'Hi guys this is my first post');
INSERT INTO posts (title, post_content) VALUES ('My Second Post', 'Hi guys this is my second post');


INSERT INTO comments (username, comment_content, post_id) VALUES ('user1', 'this post sucks', 1);
INSERT INTO comments (username, comment_content, post_id) VALUES ('user2', 'this post is so good', 1);
INSERT INTO comments (username, comment_content, post_id) VALUES ('user3', 'this post isnt bad', 1);
INSERT INTO comments (username, comment_content, post_id) VALUES ('user1', 'this post is better', 2);

