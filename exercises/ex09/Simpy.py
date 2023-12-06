"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730649407"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def init(self, values: list[float]):
        """Constructor."""
        self.values = values

    def __str__(self) -> str:
        """String method."""
        words: str = f"Simpy({self.values})"
        return words
    
    def fill(self, new_value: float, num_value: int) -> None:
        """Fill method."""
        new_list: list[float] = []
        for i in range(num_value):
            new_list.append(new_value)
            self.values = new_list

    def arrange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arrange method."""
        assert step != 0.0
        new_list: list[float] = []
        x = start
        while x != stop:
            new_list.append(x)
            x += step

    def sum(self) -> float:
        """Sum method."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add method."""
        new_list: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] + rhs.values[i])
            else:
                for idx in self.values:
                    new_list.append(idx + rhs)
            return Simpy(new_list)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Pow method."""
        new_list: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] ** rhs.values[i])
            else:
                for idx in self.values:
                    new_list.append(idx ** rhs)
            return Simpy(new_list)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Eq method."""
        new_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] == rhs.values[i])
            else:
                for idx in self.values:
                    new_list.append(idx == rhs)
            return Simpy(new_list)
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """GT method."""
        new_list: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_list.append(self.values[i] > rhs.values[i])
            else:
                for idx in self.values:
                    new_list.append(idx > rhs)
            return Simpy(new_list)
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get item method."""
        if type(rhs) is int:
            return self.values[rhs]
        else:
            new_list: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                if rhs[i] is True:
                    new_list.values.append(self.values[i])
            return Simpy(new_list)