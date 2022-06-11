"""This function is created to serve as the main routine for component 2. It
calls the choose_difficulty function and if the player choose a difficulty not
not designed, it will prompt them to choose the difficulty needed until they
choose a difficulty.
Created by Thanh Do
11/06/2022"""
def game_difficulty():


    # Set up difficulties

    input("Press 'Enter' to start: ")
    # Let the players choose one difficulty mode
    valid = False
    while not valid:
        error = "Please choose 1 in 3 difficulties!"
        try:
            print("main_function()")
            valid = True
        #If not
        except ValueError:
                print(error)

    return 'start the game'


print(game_difficulty())
