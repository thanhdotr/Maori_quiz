"""Assemble outcome v2. I  add the database import system(component 1)
and fix the error where it gives a value error if enter a non integer in
 difficulties. Also corrected the statistic where it should be the number of
 attempt, not mistake"""
import pandas as pd
import random


def import_and_split():
    # Replacement list for item that python does not read
    replacement_list = [["a", "ā"], ["e", "ē"], ["i", "ī"], ["o", "ō"],
                        ["u", "ū"]]
    word_list = []
    meaning_list = []
    category_list = []
    df = pd.read_csv('Maori Words.csv')
    word_database = df.values.tolist()
    # Replace item that python does not read (item with macron)
    for i in range(len(word_database)):
        for g in range(len(replacement_list) - 1):
            if word_database[i][3] == replacement_list[g][0] \
                    and "?" in word_database[i][1]:
                word_database[i][1] = \
                    word_database[i][1].replace("?", replacement_list[g][1])

    # split the words supplied in the database
    def spliting_function(list_needed, func):
        for g in range(len(list_needed)):
            word_list.append([i for i in list_needed[g][func]])

    spliting_function(meaning_list, 0)
    spliting_function(word_database, 1)
    spliting_function(category_list, 2)

    return word_list, meaning_list, category_list


def game_difficulty():

    # Set up difficulties
    easy = 6
    medium = 3
    hard = 2

    input("Press 'Enter' to start: ")
    # Let the players choose one difficulty mode
    valid = False
    while not valid:
        error = "Please choose 1 in 3 difficulties!"
        try:
            print(f"1 - Easy:  {easy} wrong attempts.\n"
                  f"2 - Medium:{medium} wrong attempts.\n"
                  f"3 - Hard: {hard} wrong attempts.")

            difficulty = input("Difficulties:\n"
                               "").upper()

            if difficulty == "1":
                print("You are allowed to have {} wrong!".format(easy))
                return easy

            elif difficulty == "2":
                print("You are allowed to have {} wrong!".format(medium))
                return medium

            elif difficulty == "3":
                print("You are allowed to have only {} wrong!".
                      format(hard))
                return hard

            else:
                print(error)

        except ValueError:
            print(error)


def main_game(mistakes, imported_lists):
    global word_length,attempt
    mistakes = int(mistakes)
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
    mistakes = int(mistakes)
    word_list = imported_lists[0]
    # choose a random word
    chosen_word = random.choice(word_list)
    position = word_list.index(chosen_word)
    word_length = len(chosen_word)
    attempt = 0
    correct = 0
    unused_letter = []
    display = []
    # Create a list for displaying words that needs to be guessed.
    for _ in range(word_length):
        display += "_"

    # Create a game state to determined if game had ended or not
    end_of_game = False

    while attempt != mistakes:
        # print(f"Category = {category[position-1]}")
        guess = input("Guess a letter: ").lower()
        # Check guessed letter
        while not guess.isalpha():
            print("Please enter a letter.")
            guess = input("Guess a letter: ").lower()
        if guess in display or guess in unused_letter:
            print(f"You have already guessed {guess}!")
        else:
            # If letter is in designated position, change from _ to the letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
                    correct += 1
                    print(display)
            # If the guess is not in the chosen word, increase attempt by 1 and print list
            # of not chosen word
            if guess not in chosen_word:
                attempt += 1
                unused_letter.append(guess)
                print(f"Not used letter: {unused_letter}")
                print(f"You have {mistakes - attempt} attempt(s) left")
                print(display)
        if mistakes == 6:
            print(images[attempt])
        elif mistakes == 3:
            print(images[attempt+2])
        elif mistakes == 2:
            print(images[attempt+3])
        # When there is no "_", say that the user wins.
        if "_" not in display:
            end_of_game = True
            print("                              .__ \n"
                  "___.__. ____  __ __  __  _  _|__| ____ \n"
                  "<   |  |/  _ \|  |  \ \ \/ \/ /  |/    \ \n"
                  "\___  (  <_> )  |  /  \     /|  |   |  \ \n"
                  "/ ____|\____/|____/    \/\_/ |__|___|  / \n"
                  "\/                                   \/ \n"
                  f"The word is {chosen_word}")


    # If user have not win, print the word
    if end_of_game is False:
        print("                      .__                       \n"
              " ___.__. ____  __ __  |  |   ____  ______ ____  \n"
              "<   |  |/  _ \|  |  \ |  |  /  _ \/  ___// __ \ \n"
              "\___  (  <_> )  |  / |  |_(  <_> )___ \\  ___/\n"
              "/ ____|\____/|____/  |____/\____/____  >\___  >\n"
              "\/                                   \/     \/ \n"
              "\n"
              f"The word is {chosen_word}")
    statistics()
    input("Press enter to return to main menu")



def statistics():
    stats_list = []
    total_list = []
    percentage = 1 - (attempt - 1) / word_length
    stats_list.append(attempt)
    stats_list.append(word_length)
    stats_list.append(round(percentage, 2))
    total_list.append(stats_list)
    if total_list :
        for i in range(len(total_list)):
            print(f"Player {i} got {attempt} wrong in a word with"
                  f" {word_length} letters with an accuracy of {percentage * 100}%")
def Help():
    input("Hangman for Maori Language\n"
          "- You have been given a word.\n"
          "- You need to guess its letters.\n"
          "- You can only enter 1 letter each guess.\n"
          "Note: to change your language to maori to do the macron, go to \n"
          "https://tekete.ara.ac.nz/file/fa9a9b38-aa9d-44a6-8464-e2e64ddd3842/4/Formatting-Maori-keyboard.pdf\n"
     "Press Enter to go back to the main menu")
    return ""

def main_menu():

    #Hangman title
    print(
    "  ___ ___                                                     ______"
    "_____              __               \n"
    " /   |   \_____    ____    ____   _____ _____    ____         \__   "
    " ___/____   __ ___/  |______   __ __ \n"
    "/    ~    \__  \  /    \  / ___\ /     \\__  \  /    \   ______ |    |"
    "  \__  \ |  |  \   __\__  \ |  |  \ \n"
    "\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \ /_____/ |    |"
    "   / __ \|  |  /|  |  / __ \|  |  / \n"
    " \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /         |____|"
    "  (____  /____/ |__| (____  /____/ \n"
    "       \/      \/     \//_____/       \/     \/     \/                "
    "       \/                 \/       ")
    #give players options
    print("1. Play with computer\n"
          "2. Statistic\n"
          "3. Help screen\n"
          "4. Quit game\n")
    choice = input(">> ")
    try:
        choice = int(choice)
    except ValueError:
        choice = input(">>")
    if choice == 1:
        print(main_game(game_difficulty(), import_and_split()))
        main_menu()
        statistics()
    if choice == 2:
        statistics()
        main_menu()
    if choice == 3:
        print(Help())
        main_menu()
    if choice == 4:
        print("Thank you for playing the game")
    else:
        print()
print(main_menu())

