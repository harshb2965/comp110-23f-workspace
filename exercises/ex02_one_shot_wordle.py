"""Python version to wordle game."""


__author__ = "730649407"


secret_word: str = "python"


user_guess: str = input("What is your 6-letter guess? ")


while len(user_guess) != len(secret_word):
   user_guess = input("That was not 6 letters! Try again: ")
  
guess_idx: int = 0
result_emoji: str = ""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


correct_str: bool = True


while guess_idx < len(user_guess):
   if user_guess[guess_idx] == secret_word[guess_idx]:
       result_emoji += str(GREEN_BOX)
       guess_idx += 1
   else:
       correct_str = False
       chr_exist: bool = False
       alt_idx_checker: int = 0
       while chr_exist is not True and alt_idx_checker < len(secret_word):
           if secret_word[alt_idx_checker] == user_guess[guess_idx]:
               chr_exist = True
           else:
               alt_idx_checker += 1
       if chr_exist is True:
           result_emoji += str(YELLOW_BOX)
           guess_idx += 1
       else:
           result_emoji += str(WHITE_BOX)
           guess_idx += 1


print(result_emoji)


if not correct_str:
   print("Not quite. Play again soon!")
else:
   print("Woo! You got it!")