from random import *

def game():
  number = randint(1,100)
  guesses = 8
  while True:
    try:
      guess = int(input("Choose a number between 1 to 100 : "))
      if number == guess:
        print("That's Correct")
        break
      elif number < guess:
        print("That's Too High Try Again!")
      elif number > guess:
        print("That's too low, guess again!")
      guesses -= 1
      print("You Have " +str(guesses) +" guesses left.")
    except:
        print("NUMBERS!")
    if guesses == 0:
      print("Game Over")
      print("The Number is " +str(number))
      break

game()  
