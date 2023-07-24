#################################################################
# FILE : board.py
# WRITER : amitai turkel , amitat.turkel , 314632878
# DESCRIPTION: a class Board
#################################################################

import copy
class Board:
    """
    This class represents a board for the Rush Hour puzzle game.

    Attributes:
        board (list): The 2D list representing the board with cars and empty spaces.
        _dict_car (dict): A dictionary storing Car objects with their names as keys.

    Note: Add a class description here, explaining the purpose of the class.
    """

    def __init__(self):
        """Initialize the board with default configurations."""
        board = [["_" for column in range(7)] for row in range(7)]
        board[len(board) // 2].append("E")
        self.board = board
        self._dict_car = dict()

    def __str__(self):
        """Return a string representation of the current status of the board."""
        new_board = copy.deepcopy(self.board)
        for row in range(len(self.board)):
            new_board[row].append("*")
        new_board[len(self.board) // 2].pop()
        return str(new_board)

    def cell_list(self):
        """Return a list of coordinates of all cells in this board."""
        coor_list = [(len(self.board) // 2, len(self.board[0]))]
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                coor_list.append((row, col))
        return coor_list

    def possible_moves(self):
        """Return a list of legal moves for all cars in this board."""
        legal_for_car = []
        for name in self._dict_car.keys():
            car = self._dict_car[name]
            car_coordinates = car.location
            if car.orientation == 1:  # Horizontal car
                if car_coordinates[1] + car.length < len(self.board) and self.board[car_coordinates[0]][car_coordinates[1] + car.length] == "_":
                    legal_for_car.append((name, "r", "The car can move right"))
                if car_coordinates[1] - 1 >= 0 and self.board[car_coordinates[0]][car_coordinates[1] - 1] == "_":
                    legal_for_car.append((name, "l", "The car can move left"))
            else:  # Vertical car
                if car_coordinates[0] + car.length < len(self.board) and self.board[car_coordinates[0] - 1][car_coordinates[1]] == "_":
                    legal_for_car.append((name, "u", "The car can move up"))
                if car_coordinates[0] - 1 >= 0 and self.board[car_coordinates[0] + car.length][car_coordinates[1]] == "_":
                    legal_for_car.append((name, "d", "The car can move down"))
        return legal_for_car

    def target_location(self):
        """Return the coordinates of the location to be filled for victory."""
        return len(self.board) // 2, len(self.board[0])

    def cell_content(self, coordinate):
        """
        Return the name of the car in the given coordinates, or None if the cell is empty.
        :param coordinate: A tuple of (row, col) of the coordinate to check.
        :return: The name of the car or None.
        """
        if coordinate[0] == len(self.board) // 2 and coordinate[1] == len(self.board[0]):
            if self.board[coordinate[0]][coordinate[1]][:] == "E":
                return None
            return self.board[coordinate[0]][coordinate[1]][:]
        if coordinate[0] >= len(self.board) or coordinate[0] < 0:
            return None
        if coordinate[1] >= len(self.board[0]) or coordinate[1] < 0:
            return None
        if self.board[coordinate[0]][coordinate[1]] == "_":
            return None
        else:
            return self.board[coordinate[0]][coordinate[1]][:]

    def add_car(self, car):
        """Add a car to the game board."""
        car_coordinates = car.location
        if (car_coordinates[0] < 0 or car_coordinates[0] > len(self.board)) or \
           (car_coordinates[1] < 0 or car_coordinates[1] > len(self.board[car_coordinates[0]])):
            return False
        if car.get_name() in self._dict_car.keys():
            return False
        if car.orientation == 1:  # Horizontal car
            if car_coordinates[1] + car.length > len(self.board):
                return False
            for empty in range(car_coordinates[1], car.length + car_coordinates[1]):  # Check if there is space
                if self.board[car_coordinates[0]][empty] != "_":
                    return False
            for empty in range(car_coordinates[1], car.length + car_coordinates[1]):  # Put the car on the board
                self.board[car_coordinates[0]][empty] = car.get_name()
            self._dict_car[car.get_name()] = car
            return True
        if car.orientation == 0:  # Vertical car
            if car_coordinates[0] + car.length > len(self.board):
                return False
            for empty in range(car_coordinates[0], car.length + car_coordinates[0]):  # Check if there is space
                if self.board[empty][car_coordinates[1]] != "_":
                    return False
            for empty in range(car_coordinates[0], car.length + car_coordinates[0]):  # Put the car on the board
                self.board[empty][car_coordinates[1]] = car.get_name()
            self._dict_car[car.get_name()] = car
            return True

    def move_car(self, name, move_key):
        """Move a car one step in the given direction."""
        if name not in self._dict_car.keys() or move_key not in ["r", "l", "d", "u"]:
            return False
        if move_key not in self._dict_car[name].possible_moves().keys():
            return False
        car_coor = self._dict_car[name].location
        car_len = int(self._dict_car[name].length)
        if move_key == "r":
            if car_coor[1] + car_len >= len(self.board[car_coor[0]]):
                return False
            if self.board[car_coor[0]][car_coor[1] + car_len] == "_":
                self.board[car_coor[0]][car_coor[1]] = "_"
                self.board[car_coor[0]][car_coor[1] + car_len] = name
                self._dict_car[name].move(move_key)  # Update the car's location
        if move_key == "l":
            if car_coor[1] - 1 < 0:
                return False
            if self.board[car_coor[0]][car_coor[1] - car_len + 1] == "_":
                self.board[car_coor[0]][car_coor[1] + car_len - 1] = "_"
                self.board[car_coor[0]][car_coor[1] - car_len + 1] = name
                self._dict_car[name].move(move_key)  # Update the car's location
            else:
                return False
        if move_key == "u":
            if car_coor[0] - 1 < 0:
                return False
            if self.board[car_coor[0] - 1][car_coor[1]] == "_":
                self.board[car_coor[0] + car_len - 1][car_coor[1]] = "_"
                self.board[car_coor[0] - 1][car_coor[1]] = name
                self._dict_car[name].move(move_key)  # Update the car's location
            else:
                return False
        if move_key == "d":
            if car_coor[0] + car_len >= len(self.board):
                return False
            if self.board[car_coor[0] + car_len][car_coor[1]] == "_":
                self.board[car_coor[0]][car_coor[1]] = "_"
                self.board[car_coor[0] + car_len][car_coor[1]] = name
                self._dict_car[name].move(move_key)  # Update the car's location
            else:
                return False
        return True
