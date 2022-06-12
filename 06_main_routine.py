"""Component 6- main routine. Call up other function from the main menu"""
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
        print("game_difficulty()")
    if choice == 2:
        print("statistics()")
    if choice == 3:
        print("Help()")
    if choice == 4:
        print("Thank you for playing the game")
    else:
        print()
