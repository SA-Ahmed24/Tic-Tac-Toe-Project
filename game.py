from User import User
from board import Board
from utils import refresh_screen, is_input_valid, restart


class Game:
    def __init__(self):
        self.user1 = User(input("Enter Name: Player 1 "))
        self.user2 = User(input("Enter Name: Player 2 "))

        self.board = Board()

    def run(self):
        while True:
            refresh_screen(self.board)

            x_choice = input("\n" + self.user1.name + ": Please choose a number between 1 - 9 ")
            while not is_input_valid(x_choice):
                x_choice = input("\n" + self.user1.name + ": Please choose a number between 1 - 9 ")

            self.board.update_cell(int(x_choice), "X")

            refresh_screen(self.board)

            if self.board.is_winner("X"):
                print("\n" + self.user1.name + " Wins! :) ")
                if restart(self.board):
                    continue
                else:
                    break

            if self.board.is_tie():
                print("\n Game Tied! :| ")
                if restart(self.board):
                    continue
                else:
                    break

            o_choice = input("\n" + self.user2.name + ": Please choose a number between 1 - 9 ")
            while not is_input_valid(o_choice):
                o_choice = input("\n" + self.user2.name + ": Please choose a number between 1 - 9 ")

            self.board.update_cell(int(o_choice), "O")

            if self.board.is_winner("O"):
                print("\n" + self.user2.name + " Wins! :) ")
                if restart(self.board):
                    continue
                else:
                    break

            if self.board.is_tie():
                print("\n Game Tied! :| ")
                if restart(self.board):
                    continue
                else:
                    break
