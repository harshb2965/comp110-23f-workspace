"""This is the Point class."""


from __future__ import annotations




class Point:
   """This is the public class for Point."""
   x: float
   y: float


   def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
       """Main constructor for the class of Point."""
       self.x = x_init
       self.y = y_init


   def scale_by(self, factor: int) -> None:
       """This method mutates the Point by factoring the original arguments."""
       self.x *= factor
       self.y *= factor


   def scale(self, factor: int) -> Point:
       """This method creates a new Point object that has been factored."""
       return Point(self.x * factor, self.y * factor)
  
   def __str__(self) -> str:
       """This prints out the Point in a readable way."""
       return f'x: {self.x}; y: {self.y}'
  
   def __mul__(self, factor: int | float) -> Point:
       """This returns a new Point that has been multiplied by the factor."""
       self.x *= factor
       self.y *= factor
       new_point: Point = Point(self.x, self.y)
       return new_point


   def __add__(self, value: int | float) -> Point:
       """This returns a new Point that has been added by the value."""
       self.x += value
       self.y += value
       new_point: Point = Point(self.x, self.y)
       return new_point