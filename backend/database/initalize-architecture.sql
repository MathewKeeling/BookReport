/* Users Table */
CREATE TABLE `book-report`.users (
	USER_GUID INT auto_increment NOT NULL,
	USERNAME varchar(100) NULL,
	EMAIL varchar(100) NULL,
    F_NAME varchar(100) NULL,
    L_NAME varchar(100) NULL,
	primary key (USER_GUID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

/* cache to input new additions to library */
CREATE TABLE `book-report`.intake_cache (
	BOOK_ID int AUTO_INCREMENT NOT NULL,
	ISBN10 varchar(255) NULL,
	ISBN13 varchar(255) NULL,
	TITLE varchar(255) NULL,
    AUTHOR_F_NAME varchar(255),
    AUTHOR_L_NAME varchar(255),
    YEAR varchar(255),
    SHELF varchar(255),
    USER varchar(255),
	PRIMARY KEY (BOOK_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

/* cache to store invalid books */
CREATE TABLE `book-report`.intake_cache_invalid (
	BOOK_ID int AUTO_INCREMENT NOT NULL,
	ISBN10 varchar(255) NULL,
	ISBN13 varchar(255) NULL,
	TITLE varchar(255) NULL,
    AUTHOR_F_NAME varchar(255),
    AUTHOR_L_NAME varchar(255),
    YEAR varchar(255),
    SHELF varchar(255),
    USER varchar(255),
	PRIMARY KEY (BOOK_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

/* table to store physical books in library */
CREATE TABLE `book-report`.physical_library (
	BOOK_ID int AUTO_INCREMENT NOT NULL,
	ISBN10 varchar(255) NULL,
	ISBN13 varchar(255) NULL,
	BOOK_JSON TEXT NOT NULL,
    SHELF varchar(255),
    USER varchar(255),
	PRIMARY KEY (BOOK_ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
