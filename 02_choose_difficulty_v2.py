"""Main function for choosing the difficulty of the game. This is built as a
function to ensure modularity and ease of call. This prompt the player to
choose 1 in 3 difficulty and different difficulties give them different attempt
If the player does not hoose 1 in 3 difficulty, tell the player to choose 1.
Created by Thanh Do
11/06/2022"""
def main_function():
    easy = 6
    medium = 3
    hard = 2
    print(f"1 - Easy: {easy} wrong attempts.\n"
                  f"2 - Medium:{medium} wrong attempts.\n"
                  f"3 - Hard: {hard} wrong attempts.")

    difficult_mode = input("Difficulties:\n"
                            "").upper()

    if difficult_mode == "1":
        mistakes = easy
        print("You are allowed to have {} wrong!".format(easy))

    elif difficult_mode == "2" :
        mistakes = medium
        print("You are allowed to have {} wrong!".format(medium))

    elif difficult_mode == "3" :
        mistakes = hard
        print("You are allowed to have only {} wrong!".
              format(hard))
    else:
        print("Please choose 1 in 3 difficulties")



