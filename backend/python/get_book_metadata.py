import requests
import json
from mysql_query import *

# API get request for metadata from OpenLibrary.org
def api_request_metadata(isbn):
    response = requests.get("http://openlibrary.org/isbn/{}.json".format(isbn))
    while True:
        try:
            book_metadata_json = response.json()
            return book_metadata_json 
        except json.decoder.JSONDecodeError:
            print("JSON Decoding Failed. Check ISBN.")
            break

# Retrieve an ISBN from a dictionary
def dict_to_isbn(record):
    if record['ISBN13']:
        isbn = record['ISBN13']
    elif record['ISBN10']:
        isbn = record['ISBN10']
    else:
        isbn = ''
        print("NO ISBN PROVIDED")
    return isbn

# Query for a book from intake cache table
def query_for_book():
    db = 'book-report'
    sql_query = 'SELECT * FROM intake_cache LIMIT 1'
    records = mysql_query_select(db, sql_query)
    # Removing the array that encapsulates the dictionary.
    records = records[0]
    print(records)
    return records


