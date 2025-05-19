CREATE DATABASE IF NOT EXISTS projectdb;
USE projectdb;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    opinion TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    rating INT NOT NULL
);

CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_location TEXT NOT NULL
);

CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_location TEXT NOT NULL
);


INSERT INTO reviews (username, opinion, created_at, rating) VALUES
('user1', 'test1', '2025-04-21 10:48:10', 1),
('user2', 'test2', '2025-04-21 10:48:22', 2),
('user3', 'test3', '2025-04-21 10:57:17', 5);

INSERT INTO images (file_name, file_location) VALUES
('stol1.jpeg', 'resources/examples/'),
('stol2.jpeg', 'resources/examples/'),
('stol3.jpeg', 'resources/examples/'),
('domek.jpg', 'resources/examples/'),
('ken1.png', 'resources/examples/'),
('ken2.png', 'resources/examples/'),
('ken3.png', 'resources/examples/'),
('ken4.png', 'resources/examples/'),


('face.jpg', 'resources/kenny/'),
('kenny1.jpg', 'resources/kenny/'),
('kenny2.jpg', 'resources/kenny/'),
('kenny3.jpg', 'resources/kenny/'),
('kenny4.jpg', 'resources/kenny/'),
('kenny5.jpg', 'resources/kenny/');

INSERT INTO videos (file_name, file_location) VALUES
('tik-tok1.mp4', 'resources/examples/videos/');