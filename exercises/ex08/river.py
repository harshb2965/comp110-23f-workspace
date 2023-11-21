"""File to define River class."""

__author__ = "730649407"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """This is the River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def view_river(self):
        """This will print out the day, the number of fish and the number of bears in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f'Fish population: {len(self.fish)}')
        print(f"Bear population: {len(self.bears)}")
    
    def check_ages(self):
        """This will remove fish and bears that are too old."""
        temp_fish: list = []
        for fish in self.fish:
            if fish.age <= 3:
                temp_fish.append(fish)
        self.fish = temp_fish

        temp_bear: list = []
        for bear in self.bears:
            if bear.age <= 5:
                temp_bear.append(bear)
        self.bears = temp_bear
        return None

    def remove_fish(self, amount: int):
        """This will remove dead fish."""
        for fish in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """This allows the bears to eat if there are enough fish to eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """This removes the dead bears."""
        temp_bear: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                temp_bear.append(bear)
        self.bears = temp_bear
        return None
        
    def repopulate_fish(self):
        """This adds in fish offspring."""
        num_offspring = (len(self.fish) // 2) * 4
        for offspring in range(num_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """This adds in bear offspring."""
        num_pairs = len(self.bears) // 2
        for pair in range(num_pairs):
            self.bears.append(Bear())
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """This calls the one_day function 7 times for a week."""
        for day in range(0, 7):
            self.one_river_day()
            
