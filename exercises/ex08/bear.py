"""File to define Bear class."""


class Bear:
    """This is the bear class."""
    age: int
    hunger_score: int
    
    def __init__(self, age_inp: int = 0, hunger_score_inp: int = 0):
        """This is the constructor for the Bear class."""
        self.age = age_inp
        self.hunger_score = hunger_score_inp
        return None
    
    def one_day(self):
        """This measures the food and age of each Bear per day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """This gives the hungerscore for each Bear."""
        self.hunger_score += num_fish