import turtle as t
import time
'''todo:
  * teams
  * stealing
  * find winner

'''

countries = {
    200:
    ("Is there more or less than 200 countries in the entire world?", "less"),
    400: ("What continent is the United Kingdom in?", "europe"),
    600:
    ("Which ocean is on the left side of California?", "the pacific ocean"),
    800:
    ("In what year was the Declaration of Independence published?", "1776"),
    1000: ("What is the most popular religion on the continent of Africa?",
           "christianity")
}

states = {
    200: ("Many states are in the United states of America?", "50"),
    400: ("What is the capital of New Jersey?", "trenton"),
    600:
    ("What is the biggest state in the United states of America?", "alaska"),
    800: ("How many states start with the letter a \"a\"?", "4"),
    1000: ("Which state is considered the \"first\" state?", "delaware")
}

landmarks = {
    200: ("What city is the Eiffel tower in?", "paris"),
    400:
    ("Is the Statue Of Liberty holding the torch? in her left hand or right hand?",
     "right"),
    600: ("How many heads are displayed on Mount Rushmore?", "4"),
    800: ("What country is the Colosseum in?", "italy"),
    1000: ("What year was The Golden Gate Bridge finished?", "1937")
}


def get_teams():
  teams = {}
  num_teams = input("How many teams would you like to participate?")
  for i in range(int(num_teams)):
    team_name = input("Team " + str(i + 1) + ", enter your name:")
    teams[team_name] = 0

  return teams


def draw_scoreboard(scoreboard):
  t.color("blue")
  t.penup()
  t.goto(-400, -100)

  for i, team_name in enumerate(scoreboard):
    t.goto(0, -100 - i * 25)
    t.write(team_name + ": " + str(scoreboard[team_name]),
            align="center",
            font=("Arial", 15, "normal"))


def ask_question(category, point_value):
  entry = category[point_value]
  question = entry[0]  # the question is always the first thing in the entry
  answer = entry[1]

  t.goto(0, 0)
  t.write(question, align="center", font=("Arial", 20, "bold"))
  guess = input(question + " ").lower()

  t.penup()
  t.goto(0, -100)
  if guess == answer:
    t.color("green")
    t.write("Correct!", align="center", font=("Arial", 20, "bold"))
    category.pop(point_value)  # removes the entire item from the dictionary
    return True
  else:
    t.color("red")
    t.write("Incorrect!", align="center", font=("Arial", 20, "bold"))
    return False


def get_category():
  while True:
    category = input("Which category would you like to choose from? ").lower()
    if category not in category_names:
      print("Invalid category choice!")
    elif category == "countries":
      return countries
    elif category == "states":
      return states
    elif category == "landmarks":
      return landmarks


def get_point_value(category):
  while True:
    point_value = int(
        input("Which point value would you like to guess from? "))
    if point_value not in category:
      print("Invalid point value choice!")
    else:
      return point_value


def game_over(scoreboard):
  scores = list(scoreboard.values())
  max_score = max(scores)
  winners = []

  if len(states) > 0 or len(landmarks) > 0 or len(
      countries) > 0:  # no winner yet
    return False

  for team_name in scoreboard:  # get winners
    if scoreboard[team_name] == max_score:
      winners.append(team_name)

  if len(winners) == 1:  # one winner
    print(winners[0] + " won the Jeoperdy game!")
  else:  # multiple winners
    message = "Tie between "
    for i in range(len(winners)):
      message += winners[i]
      if i < len(winners) - 1:
        message += ", "

    print(message)

  return True


def draw_board():
  for k in range(len(category_names)):  # goes through each category
    t.penup()
    t.goto(-250 + 250 * k, 150)
    t.color("black")
    t.write(category_names[k], align="center", font=("Arial", 25, "bold"))
    for i in range(len(point_values)):  # goes through each point value
      if point_values[i] in categories[k]:
        t.color("black")
      else:
        t.color("gray")

      t.goto(-250 + 250 * k, 120 - 30 * i)
      t.write(point_values[i], align="center", font=("Arial", 20, "normal"))


category_names = ["countries", "states", "landmarks"]
categories = [countries, states, landmarks]
point_values = [200, 400, 600, 800, 1000]
turn_idx = 0  # index representing whose turn it is in a list of team names
scoreboard = get_teams()
team_names = list(scoreboard)

while True:
  t.clearscreen()
  draw_board()
  draw_scoreboard(scoreboard)

  print(team_names[turn_idx] + ":")  # show current team
  category = get_category()
  point_value = get_point_value(category)

  t.clearscreen()
  t.hideturtle()
  result = ask_question(category, point_value)
  if result:  # correct answer
    scoreboard[team_names[turn_idx]] += point_value
    turn_idx = (turn_idx + 1) % len(team_names)  # switch teams

  else:  # incorrect answer, next team can steal
    turn_idx = (turn_idx + 1) % len(team_names)  # switch teams
    print(team_names[turn_idx] + ":")
    if input("Would you like to steal?(y or n)").lower() == "y":
      t.clearscreen()
      result = ask_question(category, point_value)
      if result:
        scoreboard[team_names[turn_idx]] += point_value

  if game_over(scoreboard):
    break

  time.sleep(2)

t.done()
