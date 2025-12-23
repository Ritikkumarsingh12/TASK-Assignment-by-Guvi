CREATE DATABASE IF NOT EXISTS IMDB;
USE IMDB;

CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_year INT,
    duration INT
);

/* USERS TABLE */

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

/* ARTISTS TABLE  */

CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(100)
);

/* 
   MEDIA TABLE
   (Movie → Multiple Media)
 */
 
CREATE TABLE media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    media_type ENUM('IMAGE','VIDEO'),
    media_url VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

/* 
   GENRES TABLE
 */
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50)
);

/* 
   MOVIE-GENRE TABLE
   (Many to Many)
*/
CREATE TABLE movie_genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

/* 
   REVIEWS TABLE
   (Movie → Reviews → User)
 */
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

/* 
   SKILLS TABLE
 */
CREATE TABLE skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(50)
);

/* 
   ARTIST-SKILLS TABLE
 */
CREATE TABLE artist_skills (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

/* 
   MOVIE ROLES TABLE
   (Artist → Multiple Roles in Movie)
*/
CREATE TABLE movie_roles (
    movie_id INT,
    artist_id INT,
    role_name VARCHAR(50),
    PRIMARY KEY (movie_id, artist_id, role_name),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

/* 
   INSERTING DATA
*/

/* MOVIES */
INSERT INTO movies (title, release_year, duration) VALUES
('Pathan', 2024, 148),
('Border', 1997, 195),
('Dhurandhar', 2025, 169);

/* USERS */
INSERT INTO users (username, email) VALUES
('ritik', 'ritik@gmail.com'),
('amit', 'amit@gmail.com'),
('neha', 'neha@gmail.com');

/* ARTISTS */
INSERT INTO artists (artist_name) VALUES
('Salman Khan'),
('Dharmender'),
('Ranveer Singh');

/* MEDIA */
INSERT INTO media (movie_id, media_type, media_url) VALUES
(1, 'IMAGE', 'Pathan.jpg'),
(1, 'VIDEO', 'Border_trailer.mp4'),
(2, 'IMAGE', 'Border_poster.jpg'),
(2, 'VIDEO', 'Pathan_trailer.mp4'),
(3, 'IMAGE', 'dhurandhar_poster.jpg'),
(3, 'VIDEO', 'dhurandhar_trailer.mp4');

/* GENRES */
INSERT INTO genres (genre_name) VALUES
('Sci-Fi'),
('Action'),
('Drama'),
('Romance'),
('Adventure');

/* MOVIE-GENRE */
INSERT INTO movie_genre VALUES
(1,1),
(1,2),
(2,3),
(2,4),
(3,1),
(3,5);

/* REVIEWS */
INSERT INTO reviews (movie_id, user_id, rating, comment) VALUES
(1,1,5,'roamtic movie'),
(1,2,4,'Great concept movie'),
(2,3,5,'Emotional and action'),
(3,1,5,'Science + emotions');

/* SKILLS */
INSERT INTO skills (skill_name) VALUES
('Acting'),
('Directing'),
('Producing'),
('Writing');

/* ARTIST-SKILLS */
INSERT INTO artist_skills VALUES
(1,1),
(1,3),
(2,2),
(2,4),
(3,1);

/* MOVIE ROLES */
INSERT INTO movie_roles VALUES
(1,1,'Actor'),
(1,2,'Director'),
(1,2,'Writer'),
(2,1,'Actor'),
(2,3,'Actor'),
(3,2,'Director');


SELECT * FROM movies;
SELECT * FROM users;
SELECT * FROM artists;
SELECT * FROM media;
SELECT * FROM genres;
SELECT * FROM movie_genre;
SELECT * FROM reviews;
SELECT * FROM skills;
SELECT * FROM artist_skills;
SELECT * FROM movie_roles;
