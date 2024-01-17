-- Database hbtn_0d_usa
-- Table states

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT AUTO_INCEREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
