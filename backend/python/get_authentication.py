from csv_loader import *

def get_mysql_credentials(account_id):
    credentials = csv_array('secrets\\accounts.csv')
    username, password, host = credentials[account_id][0], credentials[account_id][1], credentials[account_id][2]
    return username, password, host