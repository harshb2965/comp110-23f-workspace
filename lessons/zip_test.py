"""Test my zip function."""


__author__ = "730649407"


from lessons.zip import zip




def test_empty_lists() -> None:
   """It should return an empty dictionary if empty lists are passed."""
   assert zip([], []) == {}




def test_differing_lengths() -> None:
   """This one should return a blank dictionary the lists have different lengths."""
   assert zip(["9", "2"], ["john", "john", "john"]) == {}




def test_working_lists() -> None:
   """This should return a properly created dictionary."""
   assert zip(["Happy", "Tuesday"], ["1, 2"]) == {"Happy": 1, "Tuesdday": 2}