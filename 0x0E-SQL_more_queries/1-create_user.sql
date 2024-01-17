-- Create a user if not exists
-- Password should be set

CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;


-- All privileges on my server
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION;

-- FLUSH PRIVILEGES
FLUSH PRIVILEGES;
