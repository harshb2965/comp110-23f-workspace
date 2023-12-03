"""tree class."""

from __future__ import annotations

class ChristmasTreeFarm:
    """tree class."""
    plots: list[int]

    def __init__(self, plots: int, initial_planting : int):
        self.plots: list[int] = []
        for x in range(0, initial_planting):
            self.plots.append(1)
        for x in range(initial_planting, plots):
            self.plots.append(0)

    def plant(self, plot_idx: int) -> None:
        self.plots[plot_idx] = 1

    def growth(self) -> None:
        for tree in range(len(self.plots)):
            if tree != 0:
                tree += 1

    def harvest(self, replant: bool) -> int:
        counter: int = 0
        for tree in self.plots:
            if tree >= 5:
                counter += 1
                if replant == True:
                    tree = 1
                elif replant == False:
                    tree = 0
        return counter
    
    def __add__(self, farm2: ChristmasTreeFarm) -> ChristmasTreeFarm:
        new_plots: int = len(self.plots) + len(farm2.plots)
        new_initial_planting: int = 0
        for tree in self.plots:
            if tree != 0:
                new_initial_planting += 1
        for tree in farm2.plots:
            if tree != 0:
                new_initial_planting += 1
        return ChristmasTreeFarm(new_plots, new_initial_planting)
