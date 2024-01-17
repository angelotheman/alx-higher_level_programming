-- Database hbtn_0d_usa
-- Table cities


CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL,
	`state` INT NOT NULL,
	FOREIGN KEY(`state`) REFERENCES `states`(`id`)
);
