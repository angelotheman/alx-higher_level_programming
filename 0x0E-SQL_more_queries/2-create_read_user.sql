-- Database hbtn_0d_2
-- User user_0d_2
-- Privileges = SELECT
-- Password: user_0d_2_pwd

-- Create Database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- CREATE User and Password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant select Privilege on database
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost` WITH GRANT OPTION;

-- Flush Privileges
FLUSH PRIVILEGES;
