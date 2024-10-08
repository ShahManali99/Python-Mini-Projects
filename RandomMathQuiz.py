import random

good = ["good", "great", "awesome", "excellent"]
bad = ["horrible", "sick", "unhappy", "sad"]
ops = ['+','-','*',"/"]
score = 0
count = 0

def quiz():
  global score, count
  while True:
    operation = random.choice(ops)
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)

    user_answer = int(input(f"What is {num1} {operation} {num2} ? "))
    count +=1
    if operation == "+":
      my_answer = (num1) + (num2)
    elif operation == "-":
      my_answer = num1 - num2
    elif operation == "*":
      my_answer = num1 * num2
    else: 
      my_answer = num1 // num2

    if user_answer == my_answer:
      print("Well Done! You have the correct answer ")
      score +=1
    else:
      print("Try again! ")
      score -=1
    user_input=(input("Would you like to continue? "))
    if user_input.lower() == "no":
      break
  print(f"Your score is {score}/{count}")


def getname():
  while True:
    name = input("What is your name? ")
    if name != "": break
  return name

name = getname()
print("Hello " + name)
health = input("How are you today? ").lower().strip()
if health in good:
  print("Great to hear! ")
elif health in bad:
  print("Sorry to hear! ")
else:
  print("Okay! ")

answer = input("Are you ready for the quiz? (y/n)").lower().strip()
if answer.lower()=="y":
  print("Lets start. ")
  quiz()
else:
  print("Okay you don't take the test. ")

