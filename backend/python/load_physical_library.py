import json
from get_book_metadata import *
from load_intake_cache import insert_book

def copy_book(book_id):
    db = 'book-report'
    sql = 'INSERT INTO intake_cache_invalid (ISBN10, ISBN13, TITLE, AUTHOR_F_NAME, AUTHOR_L_NAME, YEAR, SHELF, USER) \
            SELECT ISBN10, ISBN13, TITLE, AUTHOR_F_NAME, AUTHOR_L_NAME, YEAR, SHELF, USER FROM intake_cache WHERE BOOK_ID=%s'
    args = book_id
    mysql_query(db, sql, args)

def delete_row(primary_key):
    # print(json)
    db = 'book-report'
    sql = 'DELETE FROM intake_cache WHERE book_id=%s'
    args = primary_key
    mysql_query(db, sql, args)
    print("Removed book from intake cache successfully!")

def get_json():
    book = query_for_book()
    book_json = str(json.dumps(api_request_metadata(dict_to_isbn(book))))
    return(book_json, book)

def insert_row(json):
    # print(json)
    db = 'book-report'
    sql = \
        'INSERT INTO physical_library(BOOK_JSON)\
        VALUES(\"%s")'
    args = json
    mysql_query(db, sql, args)
    print("Inserted book into database successfully!")

def insert_book_physical_library():
    json, book = get_json()
    if json == 'null':
        book_id = book['BOOK_ID']
        print(\
            "Information not found. ISBN Possibly incorrect.", \
            "\nbook_id: ", book_id, "\nISBN10: ", book['ISBN10'], "\nISBN13: ", book['ISBN13'])
        copy_book(book_id)
        delete_row(book_id)
        exit
    else:
        book_id = book['BOOK_ID']
        insert_row(json)
        delete_row(book_id)
        exit

# test
for x in range(0, 5):
    insert_book_physical_library()
