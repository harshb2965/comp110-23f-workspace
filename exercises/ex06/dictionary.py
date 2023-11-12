"""Practice with dictionary functions!"""


__author__ = "730649407"




def invert(input_dict: dict[str, str]) -> dict[str, str]:
   """Given a dictionary, it will return an inverted dictionary."""
   result_dict: dict[str, str] = {}


   for key in input_dict:
       value = input_dict[key]


       if value in result_dict:
           raise KeyError("There is a duplicate value in the dictionary!")
       else:
           result_dict[value] = key


   return result_dict




def favorite_color(colors: dict[str, str]) -> str:
   """Given a dictionary, it will return the most liked color."""
   new_list = []
   for i in colors:
       new_list.append(colors[i])
   new_dict = count(new_list)
   most_color = ""
   max_count = 0
   for color in new_dict:
       if new_dict[color] > max_count:
           max_count = new_dict[color]
           most_color = color
   return most_color




def count(inp_list: list[str]) -> dict[str, int]:
   """Given a list, it will return a dictionary that counts the items in hte input list."""
   result_dict: dict[str, int] = {}
   for key in inp_list:
       if key in result_dict:
           result_dict[key] += 1
       else:
           result_dict[key] = 1


   return result_dict




def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
   """Given a list, it will return a dictionary of letts and the list of words that belong to that letter."""
   result_dict: dict[str, list[str]] = {}
  
   for word in inp_list:
       letter = word[0]
       letter = letter.lower()


       if letter not in result_dict:
           result_dict[letter] = []
       result_dict[letter].append(word)


   return result_dict




def update_attendance(inp_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
   """Given a dictionary, it will return a dictionary that adds students to existing attendance information."""
   if day in inp_dict:
       if student not in inp_dict[day]:
           inp_dict[day].append(student)
   else:
       inp_dict[day] = [student]
   return inp_dict