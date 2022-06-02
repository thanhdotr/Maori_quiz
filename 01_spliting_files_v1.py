import pandas as pd

list1= [["a","ā"],["e","ē"],["i","ī"],["o","ō"],["u","ū"]]
list2 = []
df = pd.read_csv('Maori Words.csv')
Word_database = df.values.tolist()
print("The contents of the above file is as follows:")

for i in range (len(Word_database)):
    for g in range (len(list1)-1):
        if Word_database[i][3] == list1[g][0] and "?" in Word_database[i][1]:
            Word_database[i][1] = Word_database[i][1].replace("?",list1[g][1])
    print(Word_database[i])
def spliting_function(list_needed):
    for g in range (len(list_needed)):
        list2.append([i for i in list_needed[g][1]])
spliting_function(Word_database)
print(list2)
