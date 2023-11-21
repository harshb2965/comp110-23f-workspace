"""File to define Fish class."""


class Fish:
    """This is the Fish class."""
    age: int
    
    def __init__(self, age_inp: int = 0):
        """This is the constructor for the Fish."""
        self.age = age_inp
        return None
    
    def one_day(self):
        """This calculates the increase in the fishes' ages."""
        self.age += 1
        return None