"""function to read from a csv file using built in csv.
Created by Thanh Do
1/06/2022"""
import csv

def csv_reading():
    Word_database = []
    c = open('Maori Words.csv','r')
    o = csv.reader(c)
    print("The contents of the above file is as follows:")
    for r in o:
        print(r)
        Word_database.append(r)
    c.close()



