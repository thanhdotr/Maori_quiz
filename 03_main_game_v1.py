"""First version of the main game of hangman. This takes a random word in a
word list, make the user guess the word. If they got it right, change from "_"
to the word added, if not, don't change anything. Gives user 7 attempts.
Created by Thanh Do
12/06/2022"""
import random

word_list = ["one", "two", "three", "four", "five", "six"]
#choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
attempt = 0
#Create a list for displaying words that needs to be guessed.
display = []
for _ in range(word_length):
    display += "_"
#Create a game state to determined if game had ended or not
end_of_game = False

while attempt != 7:
    guess = input("Guess a letter: ").lower()
    #If letter is in designated position, change from _ to the letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
#If the guess is not in the chosen word, increase attempt by 1.
    if guess not in chosen_word:
        attempt += 1
        print(display)
#When there is no "_", say that the user wins.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    # print(images[attempt])
if end_of_game == False:
    print(f"You lose!, the word is {chosen_word}")
