import random
import time
import os

score = 0
choose_number = 100
visiblility_sec = 4
computer = [0]
player = [0]

level = input("Easy, Medium, Hard, or Bonus(does not have to be uppercase):  ")

if level.lower() == 'bonus':
  visiblility_sec = 5
elif level.lower() == 'medium':
  player = [0] * 2
  computer = [0] * 2
  choose_number = 1000
elif level.lower() == 'hard':
  player = [0] * 3
  computer = [0] * 3
  choose_number = 1000

while True and visiblility_sec > 0:
  for i in range(len(computer)):
    computer[i] = random.randint(1, choose_number)
  print(computer)
  time.sleep(visiblility_sec)
  os.system("clear")
  for i in range(len(computer)):
    player[i] = int(input("Enter the number you saw on the screen: "))
  if player == computer:
    print("Hooray, you got it right!")
    score = score + 1
    os.system("clear")
  else:
    print(computer)
    print("Boooooo! You suck!")
    break
  if level.lower() == "bonus":
    visiblility_sec -= 0.5
print("You final score is:", score)
