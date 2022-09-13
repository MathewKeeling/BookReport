from mysql_query import *
from csv_loader import *

def insert_book(row, owner = 'Test'):
    """CSV Format 
       0       1       2     3                 4      5         6    7
       ISBN-10,ISBN-13,TITLE,AUTHOR_FIRST_NAME,AUTHOR_LAST_NAME,YEAR,SHELF
    """
    db = 'book-report'
    sql_query = \
        'INSERT INTO intake_cache (ISBN10, ISBN13, TITLE, AUTHOR_F_NAME, AUTHOR_L_NAME, YEAR, SHELF, USER) \
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    args = row[0], row[1], row[2], row[3], row[4], row[5], row[6], owner
    mysql_query(db, sql_query, args)
    exit

def insert_books_intake_cache(books_csv = "library-csv/complete-db.csv"):
    books = csv_array(books_csv)
    for x in range(1, (len(books) - 1)):
        print(books[x])
        insert_book(books[x], 'book_intake')
    exit

# insert_books_intake_cache('library-csv/library-test.csv')


