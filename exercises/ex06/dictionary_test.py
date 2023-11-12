"""Unit Tests for dictionaries!"""


__author__ = "730649407"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


import pytest




def test_invert() -> None:
   """Inverts all elements."""
   assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}




def test_invert_empty() -> None:
   """Returns blank dictionary."""
   assert invert({}) == {}




def test_invert_keyerror() -> None:
   """Checks when keyraise error is relevant."""
   with pytest.raises(KeyError):
       my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
       invert(my_dictionary)




def test_favorite_empety() -> None:
   """r=Returns a blank dictionary."""
   assert favorite_color({}) == {}




def test_favorite_common() -> None:
   """Retunrs most popular color."""
   assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"




def test_favorite_same_color() -> None:
   """Returns only popular color."""
   assert favorite_color({"Ezri": "blue", "Kris": "blue"}) == "blue"




def test_count_empty() -> None:
   """Stores black dictionary."""
   assert count([]) == {}




def test_count_items() -> None:
   """Stores numerica values as str values as well."""
   assert count(["blue", "green", "blue"]) == {"blue": 2, "green": 1}




def test_count_same() -> None:
   """Returns only color."""
   assert count(["1", "1", "1"]) == {"1": 3}




def test_alphabetizer_empty() -> None:
   """Returns blank list."""
   assert alphabetizer([]) == {}




def test_alphabetizer_items() -> None:
   """Passes a dictionary with used letter and their systematic counts."""
   assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}




def test_alphabetizer_same() -> None:
   """Passes a dictionary with used letter and their systematic counts."""
   assert alphabetizer(["Python", "sugar", "Turtle", "party", "table"]) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}




def test_attendance_empty() -> None:
   """Returns blank dictionary."""
   assert update_attendance({}, "", "") == {"": [""]}




def test_attendance_old_students() -> None:
   """Returns added students."""
   assert update_attendance({"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}, "Wednesday", "Vrinda") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Vrinda"]}




def test_attendance_old_dayss() -> None:
   """Returns added days for students."""
   assert update_attendance({"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}, "Tuesday", "Vrinda") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}