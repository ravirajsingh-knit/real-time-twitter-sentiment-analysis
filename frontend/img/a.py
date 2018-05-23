import csv

with open('A.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    print(reader)
