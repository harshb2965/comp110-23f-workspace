"""This is a structured approach to Wordle!"""


__author__ = "730649407"




def contains_char(searched_word: str, single_chr: str) -> bool:
   """This function checks whether a guessed character exists within the word."""
   assert len(single_chr) == 1
   counter: int = 0
   while counter < len(searched_word):
       if searched_word[counter] == single_chr:
           return True
       else:
           counter += 1
   return False




WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"




def emojified(guess_word: str, secret_word: str) -> str:
   """This function returns the emojified string."""
   assert len(guess_word) == len(secret_word)
  
   guess_idx: int = 0
   result_emoji: str = ""


   while guess_idx < len(guess_word):
       if guess_word[guess_idx] == secret_word[guess_idx]:
           result_emoji += str(GREEN_BOX)
           guess_idx += 1
       elif contains_char(secret_word, guess_word[guess_idx]):
           result_emoji += str(YELLOW_BOX)
           guess_idx += 1
       else:
           result_emoji += str(WHITE_BOX)
           guess_idx += 1


   return result_emoji




def input_guess(expected_length: int) -> str:
   """Checks the length of user input."""
   user_guess: str = input(f"Enter a {expected_length} character word: ")
   while len(user_guess) != expected_length:
       user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
   return user_guess




def main() -> None:
   """The entrypoint of the program and main game loop."""
   secret_word: str = "codes"
   has_won: bool = False
   turns: int = 1


   while turns <= 6 and has_won is not True:
       print(f"=== Turn {turns}/6 ===")
       user_guess: str = input_guess(len(secret_word))
       print(emojified(user_guess, secret_word))
       if user_guess == secret_word:
           print(f"You won in {turns}/6 turns!")
           has_won = True
       else:
           turns += 1
   if has_won is not True:
       print("X/6 - Sorry, try again tomorrow!")




if __name__ == "__main__":
   main()