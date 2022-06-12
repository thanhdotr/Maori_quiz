"""Second version of the hangman game. Added letter checker, check if the user
have guessed the answer or not and add an unused letter list so that user can
see if it's """
import random
word_list = ["one", "two", "three", "four", "five", "six"]
#choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
attempt = 0
unused_letter = []
display = []
#Create a list for displaying words that needs to be guessed.
for _ in range(word_length):
    display += "_"

#Create a game state to determined if game had ended or not
end_of_game = False

while attempt != 7:
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    while not guess.isalpha():
        print("Please enter a letter.")
        guess = input("Guess a letter: ").lower()
    if guess in display or guess in unused_letter:
        print(f"You have already guessed {guess}!")
    else:
        #If letter is in designated position, change from _ to the letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(display)
#If the guess is not in the chosen word, increase attempt by 1 and print list
# of not chosen word
        if guess not in chosen_word:
            attempt += 1
            unused_letter.append(guess)
            print(f"Not used letter: {unused_letter}")
            print(display)
#When there is no "_", say that the user wins.
    if "_" not in display:
        end_of_game = True
        print("You win!")
        break
#If user have not win, print the word
if end_of_game == False:
    print(f"You lose!, the word is {chosen_word}")
