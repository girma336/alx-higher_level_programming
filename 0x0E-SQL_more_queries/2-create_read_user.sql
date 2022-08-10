-- cteate database hbtn_0d_2
CREATE DATABASES IF NOT EXISTS user_02_0;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'
GRANT SELECT ON user_02_0.* TO 'user_0d_2'@'localhost';

