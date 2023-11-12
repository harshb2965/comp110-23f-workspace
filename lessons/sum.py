"""Summing the elements of a list using different loops."""


__author__ = "730649407"




def w_sum(vals: list[float]) -> float:
   """Returns the sum of a list of floats."""
   if len(vals) == 0:
       return 0.0
   else:
       counter: int = 0
       sum: float = 0.0
       while counter < len(vals):
           sum += vals[counter]
           counter += 1
       return sum




def f_sum(vals: list[float]) -> float:
   """Returns the sum of a list of floats using a for loop."""
   if len(vals) == 0:
       return 0.0
   else:
       sum: float = 0.0
       for element in vals:
           sum += element
       return sum




def f_range_sum(vals: list[float]) -> float:
   """Returns the sum of a list of floats using a for loop and the range function."""
   if len(vals) == 0:
       return 0.0
   else:
       sum: float = 0.0
       for element in range(len(vals)):
           sum += vals[element]
       return sum