from random import randint

class Die:
    """class representing throwing of die"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides


    def roll(self):
        """return random integer between 1 and 6"""
        return randint(1, self.num_sides)