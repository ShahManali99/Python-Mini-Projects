import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random as rd

wrongGuesses = 0

print("Please think of a number between 11 and 99 but don't tell me")
lowGuess = 11
highGuess = 99
while True:
  random_num = rd.randint(lowGuess, highGuess)
  print(f'Is your number {random_num}?')
  answer = input("yes or no: ")
  if answer == ("yes"):
    plt.imshow(mpimg.imread('AI.jpeg'))
    plt.title("The AI's Brain")
    plt.axis('off')
    plt.show()
    plt.figure(figsize=(5, 2))
    break
  else:
    wrongGuesses = wrongGuesses + 1
    print("Agh, this is going to take forever")
    higherOrLower = input("is it higher or lower: ")
    if higherOrLower.lower() == "higher":
      lowGuess = random_num + 1
    else:
      highGuess = random_num - 1
  if wrongGuesses > 6:
    plt.imshow(mpimg.imread('Thumb.jpeg'))
    plt.title("Your Brain")
    plt.axis('off')
    plt.show()
    plt.figure(figsize=(5, 2))
    break

print(f'This is the number of wrong guesses so far: {wrongGuesses}')
