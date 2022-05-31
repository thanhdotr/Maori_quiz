import pandas as pd
import csv
from time import time

def pandas_reading():
    Word_database = []
    print("The contents of the above file is as follows:")
    df = pd.read_csv('Maori Words.csv')
    # print(df)
    Word_database = df.values.tolist()
    print(Word_database)

def csv_reading():
    Word_database = []
    c = open('Maori Words.csv','r')
    o = csv.reader(c)
    print("The contents of the above file is as follows:")
    for r in o:
        print(r)
        Word_database.append(r)
    c.close()

t0 = time()
pandas_reading()
t1 = time()
csv_reading()
t2 = time()

print ('function pandas_reading takes %f' %(t1-t0))
print ('function csv_reading takes %f' %(t2-t1))

