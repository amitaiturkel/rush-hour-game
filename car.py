# FILE : car.py
# WRITER : amitai turkel

class Car:
    """
    This class represents a Car object in the Rush Hour puzzle game.

    Attributes:
        __name (str): The name of the car.
        length (int): The length of the car.
        location (tuple): The head (row, col) location of the car.
        orientation (int): One of either 0 (VERTICAL) or 1 (HORIZONTAL).

    Note: Add a class description here, explaining the purpose of the class.
    """

    def __init__(self, name, length, location, orientation):
        """Constructor for a Car object."""
        self.__name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def __len__(self):
        """Return the length of the car."""
        return self.length

    def car_coordinates(self):
        """Return a list of coordinates the car occupies."""
        car_coor = []
        if self.orientation == 1:
            for place in range(self.length):
                car_coor.append((self.location[0], self.location[1] + place))
        if self.orientation == 0:
            for place in range(self.length):
                car_coor.append((self.location[0] + place, self.location[1]))
        return car_coor

    def possible_moves(self):
        """Return a dictionary of strings describing possible movements permitted by this car."""
        move_dict = dict()
        if self.orientation == 1:  # Horizontal car
            move_dict["l"] = "The car can move left"
            move_dict["r"] = "The car can move right"
        if self.orientation == 0:  # Vertical car
            move_dict["u"] = "The car can move up"
            move_dict["d"] = "The car can move down"
        return move_dict

    def movement_requirements(self, move_key):
        """Return a list of cell locations which must be empty for this move to be legal."""
        if move_key == "l":
            req = [(self.location[0], self.location[1] - 1)]
            return req[:]
        if move_key == "r":
            req = [(self.location[0], self.location[1] + self.length)]
            return req[:]
        if move_key == "d":
            req = [(self.location[0] + self.length, self.location[1])]
            return req[:]
        if move_key == "u":
            req = [(self.location[0] - 1, self.location[1])]
            return req[:]

    def move(self, move_key):
        """Move the car one step in the given direction."""
        if self.orientation == 1:  # Horizontal car
            if move_key in ["r", "l"]:
                if move_key == "l":
                    self.location = (self.location[0], self.location[1] - 1)
                    return True
                if move_key == "r":
                    self.location = (self.location[0], self.location[1] + 1)
                    return True
            else:
                return False
        if self.orientation == 0:  # Vertical car
            if move_key in ["d", "u"]:
                if move_key == "d":
                    self.location = (self.location[0] + 1, self.location[1])
                    return True
                if move_key == "u":
                    self.location = (self.location[0] - 1, self.location[1])
                    return True
            else:
                return False

    def get_name(self):
        """Return the name of this car."""
        name = self.__name
        return name[:]
