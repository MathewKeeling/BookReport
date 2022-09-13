import pymysql
from get_authentication import *
from csv_loader import *

# Helpful websites:
# https://o7planning.org/11463/connect-to-mysql-database-in-python-using-pymysql
# https://realpython.com/python-mysql/
# https://zetcode.com/python/pymysql/ 
# https://stackoverflow.com/questions/1633332/how-to-put-parameterized-sql-query-into-variable-and-then-execute-in-python

def mysql_query(sql_db, sql_query, args):
    sql_username, sql_password, sql_host = get_mysql_credentials(1)
    connection = pymysql.connect(host=sql_host,
                                user=sql_username,
                                password=sql_password,                             
                                db=sql_db,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor) 
    try:  
        with connection.cursor() as cursor: 
            cursor.execute(sql_query, args, )
            print ("cursor.description: ", cursor.description, "\n") 
            for row in cursor:
                print(row)
            connection.commit()
    finally:
        connection.close()

def mysql_query_select(sql_db, sql_query):
    sql_username, sql_password, sql_host = get_mysql_credentials(1)
    connection = pymysql.connect(host=sql_host,
                                user=sql_username,
                                password=sql_password,                             
                                db=sql_db,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor) 
    try:  
        with connection.cursor() as cursor: 
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return(result)
        
    finally:
        connection.close()


        
