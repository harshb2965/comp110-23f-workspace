"""Combining two lists into a dictionary."""


__author__ = "730649407"




def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
   """This function takes in 2 lists and returns them as a dictionary."""
   temps: dict[str, int] = {}
   if len(list1) != len(list2):
       return temps
   elif len(list1) == 0 or len(list2) == 0:
       return temps
   else:
       counter: int = 0
       for elem in list1:
           temps[elem] = list2[counter]
           counter += 1
       return temps