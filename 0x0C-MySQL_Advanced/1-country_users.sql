-- Script that creates a table with some requirements
-- Add task 1

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL
);
