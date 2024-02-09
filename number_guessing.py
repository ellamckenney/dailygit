import random

random_number = random.randint(1, 500)

guess_limit = 5
guesses = 0
won = False

while guesses < guess_limit and not won:
  try:
    guess = int(input("Guess a number between 1 and 500: "))
  except ValueError:
    print("Input is invalid. Please enter a number.")
    continue
  
  guesses += 1
  if guess == random_number:
    won = True 
    print(f"⁺˚⋆｡°✩₊✧˖°˖⁺‧₊˚✦⋆ ˚｡CONGRATS⁺˚⋆｡°✩₊✧˖°˖⁺‧₊˚✦⋆ ˚｡\nYou guessed the number in {guesses} attempts!")
  elif guess < random_number:
    print("Your guess is too low, try again!")
  elif guess > random_number:
    print("Your guess is too high, try again!")
    
  remaining_guesses = guess_limit - guesses
  print(f"You have {remaining_guesses} guesses left.")
  
  if not won:
    print(f"You ran out of guesses! The number was {random_number}.")