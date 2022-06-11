"""This is the """

def main_function():
    easy = 6
    medium = 3
    hard = 2
    print(f"1 - Easy:  {easy} wrong attempts.\n"
                  f"2 - Medium:{medium} wrong attempts.\n"
                  f"3 - Hard: {hard} wrong attempts.")

    difficulty = input("Difficulties:\n"
                            "").upper()

    if difficulty == "1":
        main_function().mistakes = easy
        print("You are allowed to have {} wrong!".format(easy))

    elif difficulty == "2" :
        main_function().mistakes = medium
        print("You are allowed to have {} wrong!".format(medium))

    elif difficulty == "3" :
        main_function().mistakes = hard
        print("You are allowed to have only {} wrong!".
              format(hard))
    else:
        print(error)


def game_difficulty():

    global mistakes, difficulty, error
    # Set up difficulties

    input("Press 'Enter' to start: ")
    # Let the players choose one difficulty mode
    valid = False
    while not valid:
        error = "Please choose 1 in 3 difficulties!"
        try:
            main_function()
            valid = True

        except ValueError:
                print(error)

    return 'start the game'


print(game_difficulty())
