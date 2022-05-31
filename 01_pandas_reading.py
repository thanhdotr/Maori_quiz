import pandas as pd
# A function to read the
def pandas_reading():
    Word_database = []
    print("The contents of the above file is as follows:")
    df = pd.read_csv('Maori Words.csv')
    # print(df)
    Word_database = df.values.tolist()
    print(Word_database)
