"""List Utility Function."""


__author__ = "730649407"




def all(int_list: list[int], checker: int) -> bool:
   """Given a list, returns bool whether all ints in the list match the given int."""
   if len(int_list) == 0:
       return False
   else:
       counter: int = 0
       while counter < len(int_list):
           if int_list[counter] != checker:
               return False
           counter += 1
       return True




def max(int_list: list[int]) -> int:
   """Given a list, returns the largest element in the list."""
   if len(int_list) == 0:
       raise ValueError("max() arg is an empty List")
   max: int = int_list[0]
   counter: int = 1
   while counter < len(int_list):
       if int_list[counter] > max:
           max = int_list[counter]
       counter += 1
   return max




def is_equal(list_1: list[int], list_2: list[int]) -> bool:
   """Given two lists, returns bool whether every element matches at every index."""
   if len(list_1) != len(list_2):
       return False
   else:
       counter: int = 0
       while counter < len(list_1):
           if list_1[counter] != list_2[counter]:
               return False
           counter += 1
   return True