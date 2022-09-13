import csv

def csv_array(file):
    with open(file, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data