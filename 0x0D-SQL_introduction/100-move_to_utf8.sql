-- Convert to utf8mb4 collate utf8mb4_unicode_ci

USE	`hbtn_0c_0`
ALTER `first_table`
MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;