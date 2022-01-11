from pandas import *

data = read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter any word of your choice: ")
print("\nThe phonetic words associated with your input are:")
for alphabet in user_input:
    for (key, value) in dict.items():
        if alphabet.upper() == key:
            print(value)
