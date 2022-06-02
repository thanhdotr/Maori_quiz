"""This is a function to test to see if the function that runs with the use of
the pandas library(pandas_reading) is faster or the one without pandas library
(csv_reading) is faster"""
import pandas as pd
import csv
from time import time

def pandas_reading():#function that reads the csv file using pandas
    Word_database = []
    print("The contents of the above file is as follows:")
    df = pd.read_csv('Maori Words.csv')
    # print(df)
    Word_database = df.values.tolist()
    print(Word_database)

def csv_reading(): #function that reads the csv file using built-in csv reader
    Word_database = []
    c = open('Maori Words.csv','r')
    o = csv.reader(c)
    print("The contents of the above file is as follows:")
    for r in o:
        print(r)
        Word_database.append(r)
    c.close()
#Time measuring. T0 represent the start time, T1 represent the runtime for
#pandas_reading function while T2 represent the runtime for csv_reading
# function

t0 = time()
pandas_reading()
t1 = time()
csv_reading()
t2 = time()

print ('function pandas_reading takes %f' %(t1-t0))
print ('function csv_reading takes %f' %(t2-t0))

