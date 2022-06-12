"""This function uses the pandas library to import and split word from the
imported file. Have a replacement function that can be utilised when needed to
 change word as python cannot read maori's macron.
Created by Thanh Do
"""
import pandas as pd
#Replacement list for item that python does not read
replacement_list= [["a","ā"],["e","ē"],["i","ī"],["o","ō"],["u","ū"]]
word_list = []
df = pd.read_csv('../Maori Words.csv')
Word_database = df.values.tolist()
print("The contents of the above file is as follows:")
#Replace item that python does not read (item with macron)
for i in range (len(Word_database)):
    for g in range (len(replacement_list)-1):
        if Word_database[i][3] == replacement_list[g][0] and "?" in Word_database[i][1]:
            Word_database[i][1] = Word_database[i][1].replace("?",replacement_list[g][1])
    print(Word_database[i])
#split the words supplied in the database
def spliting_function(list_needed):
    for g in range (len(list_needed)):
        word_list.append([i for i in list_needed[g][1]])
spliting_function(Word_database)
print(word_list)
