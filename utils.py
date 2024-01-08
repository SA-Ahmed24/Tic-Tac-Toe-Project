import os


def is_input_valid(choice):
    if not choice.isnumeric():
        print("this is not a valid number")
        return False
    elif int(choice) > 9 or int(choice) < 1:
        print("This number is not in range of 1-9")
        return False
    else:
        return True


os.system("Clear")


def refresh_screen(board):
    os.system("clear")
    board.display()


def restart(board):
    play_again = input("Would you like to play again? (Y/N)").upper()
    if play_again == "Y":
        board.reset()
        return True
    else:
        return False
