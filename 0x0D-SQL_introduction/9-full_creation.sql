-- Create a new table
-- Create multiple rows in that table
-- Table name = second_table

CREATE TABLE IF NOT EXISTS `second_table` (
	`id` INT,
	`name` VARCHAR(256),
	`score` INT
);


-- Create multiple rows in the table
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "George", 8);
