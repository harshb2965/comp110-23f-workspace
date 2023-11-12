"""EX01 - Chardle - A cute step toward Wordle."""


__author__ = "730649407"


counter: int = 0


input_word: str = input("Enter a 5-character word: ")
if len(input_word) != 5:
   print("Error: Word must contain 5 characters")
   exit()
else:
   input_chr: str = input("Enter a single character: ")
   if len(input_chr) != 1:
       print(" Error: Character must be a single character.")
       exit()
   else:
       print("Searching for " + input_chr + " in " + input_word)
       if input_word[0] == input_chr:
           print(input_chr + " found at index 0")
           counter += 1
       if input_word[1] == input_chr:
           print(input_chr + " found at index 1")
           counter += 1
       if input_word[2] == input_chr:
           print(input_chr + " found at index 2")
           counter += 1
       if input_word[3] == input_chr:
           print(input_chr + " found at index 3")
           counter += 1
       if input_word[4] == input_chr:
           print(input_chr + " found at index 4")
           counter += 1


       if counter == 0:
           print("No instances of " + input_chr + " found in " + input_word)
       else:
           if counter == 1:
               print("1 instance of " + input_chr + " found in " + input_word)
           else:
               print(str(counter) + " instances of " + input_chr + " found in " + input_word)