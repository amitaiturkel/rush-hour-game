# FILE : game.py
# WRITER : amitai turkel

import json
import sys
from board import Board
from car import Car

class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board
        self.cars = list()

    def get_file_with_cars(self, path):
        """Read cars configurations from a JSON file and add them to the game."""
        json_file = path
        with open(json_file, 'r') as file:
            car_con = json.load(file)

        for car in car_con.keys():
            self.cars.append(Car(car, car_con[car][0], car_con[car][1], car_con[car][2]))

    def place_cars(self):
        """Place the cars on the board."""
        for car in self.cars:
            self.board.add_car(car)

    def __single_turn(self):
        """Run one turn of the game."""
        valid = False
        first_letter = "YBOGWR"
        sec_letter = "udlr"
        while not valid:
            move = input("Which car do you want to move? Please answer in the format 'Y,d': ")
            if len(move) == 3 and move[0] in first_letter and move[1] == "," and move[2] in sec_letter:
                valid = True
            else:
                print("Invalid input. Try again.")
            if move == "!":
                exit(0)

        self.board.move_car(move[0], move[2])

    def play(self):
        """Play the game until completion."""
        if self.board.board[len(self.board.board) // 2][len(self.board.board[0])] != "E":
            print("Game is over.")
            return None
        while self.board.board[len(self.board.board) // 2][len(self.board.board[0])] == "E":
            print(str(self.board))
            self.__single_turn()
        print("The game is over!")

if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.get_file_with_cars(sys.argv[1])
    game.place_cars()
    game.play()
