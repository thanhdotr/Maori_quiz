"""Third version of the hangman game. Added some graphics and a attempt counter
for the game.
Created by Thanh Do.
12/06/2022"""
def main_game(mistakes):
    import random

    images = ['''
                ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||ˍ
              | |          (\\__৲
              | |           `--ˊ
              | |
              | |
              | |
              | |
              | |
              | |
              | |
              | |
              | |
              ''', '''
                ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |
              | |
              | |
              | |
              | |
              | |
              | |
              | |
              | |
    ''', '''
        ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |         .-`--'.
              | |         Y . . Y
              | |          |   |
              | |          | . |
              | |          |   |
              | |
              | |
              | |
              | |
              | |
    ''', '''
      ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |         .-`--'.
              | |        /Y . . Y
              | |       // |   |
              | |      //  | . |
              | |     ')   |   |
              | |
              | |
              | |
              | |
              | |
    ''', '''
                ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |         .-`--'.
              | |        // . . \\
              | |       // |   | \\
              | |      //  | . |  \\
              | |     ')   |   |   (`
              | |
              | |
              | |
              | |
    ''', '''
      ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |         .-`--'.
              | |        // . . \\
              | |       // |   | \\
              | |      //  | . |  \\
              | |     ')   |   |   (`
              | |          ||-
              | |          ||
              | |          ||
              | |          ||
              | |         / |
    ''', '''
    
      ___________.._______
              | .__________))______|
              | | / /      ||
              | |/ /       ||
              | | /        ||
              | |/         ||
              | |          ||.-''.
              | |          |/  _  \\
              | |          ||  ☉/☉|
              | |          (\\◝_ .'
              | |           `--'
              | |         .-`--'.
              | |        // . . \\
              | |       // |   | \\
              | |      //  | . |  \\
              | |     ')   |   |   (`
              | |          ||-||
              | |          || ||
              | |          || ||
              | |          || ||
              | |         / | | \
    ''']
    word_list = []
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

    while attempt != mistakes:
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
                print(f"You have {mistakes - attempt} attempt(s) left")
                print(display)
    #When there is no "_", say that the user wins.
        if "_" not in display:
            end_of_game = True
            print("                              .__ \n"        
                "___.__. ____  __ __  __  _  _|__| ____ \n"
                "<   |  |/  _ \|  |  \ \ \/ \/ /  |/    \ \n" 
                "\___  (  <_> )  |  /  \     /|  |   |  \ \n"
                "/ ____|\____/|____/    \/\_/ |__|___|  / \n"
                "\/                                   \/ \n")
            break

    #If user have not win, print the word
    if end_of_game == False:
        print("                      .__                       \n"
                 " ___.__. ____  __ __  |  |   ____  ______ ____  \n"
                 "<   |  |/  _ \|  |  \ |  |  /  _ \/  ___// __ \ \n"
                 "\___  (  <_> )  |  / |  |_(  <_> )___ \\  ___/\n" 
                 "/ ____|\____/|____/  |____/\____/____  >\___  >\n"
                 "\/                                   \/     \/ \n"
              "\n"
              f"The word is {chosen_word} ")
