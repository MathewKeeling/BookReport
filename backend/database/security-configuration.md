# Initializing the Database

## Accessing the SQL Database for Initial Configuration
```sh
# shell into the container
docker exec -it $mysql_db_name /bin/bash
mysql -u root -p
```

## The MySQL DB
```sql
/* List Databases */
SHOW DATABASES;

/* Create Databases */
CREATE DATABASE TEST;

/* Delete Databases */

/* Show users */
SELECT USER FROM mysql.user

/* Create User Account */
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'the_secure_password';

/* Delete User account */
DROP USER 'user'@'localhost';

/* Grant Privileges: DO NOT USE */
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION

/* Alter User IP */
UPDATE mysql.user SET Host='%' WHERE Host='localhost' AND User='username';


```