import os


def printgameboard(gameboard):
  for row in range(0, len(gameboard)):
    print(gameboard[row])
    print()
  print("   1     2     3     4     5     6     7")


def playerturn(gameboard, player):
  print("player turn ", player)
  while True:
    print("enter a col 1 - 7")
    col = input()
    if col.isnumeric():
      col = int(col)
      if 1 <= col <= 7:
        col -= 1
        if gameboard[0][col] == "  ":
          for row in range(len(gameboard) - 1, -1, -1):
            if gameboard[row][col] == "  ":
              gameboard[row][col] = player
              return row, col
        else:
          print("Column is full. Choose another one.")
      else:
        print("Please enter a number between 1 and 7.")
    else:
      print("Please enter a valid number.")


# def playerturn(gameboard , player):
#   print("player turn ", player)
#   while True:

#     col = 0
#     while True:
#       print ("enter a col 1 - 7")
#       col = input()
#       if col.isnumeric():
#         col = int(col)
#         if col >=1 and col <=7:
#           col -=1
#           break
#     if gameboard[0][col]!="  ":
#       print("choose a other one")
#       continue

#     for row in range(len(gameboard)):
#       if gameboard[row + 1][col]!="  ":
#         gameboard[row][col]=player
#         return row, col
#       elif row == len(gameboard) - 2:
#         gameboard[row + 1][col]=player
#         return row + 1, col
#     break


def is_board_full(gameboard):
  return all(cell != "  " for row in gameboard for cell in row)


def Horizontal_check(row, player):
  count = 0
  for col in range(0, 7):
    piece = gameboard[row][col]
    if piece == "  " or gameboard[row][col] != player:
      count = 0
      continue
    elif player == piece:
      count += 1
      if count == 4:
        return True
  return False


def Vertical_check(col, player):
  count = 0
  for row in range(0, 6):
    piece = gameboard[row][col]
    if piece == "  " or gameboard[row][col] != player:
      count = 0
      continue
    elif player == piece:
      count += 1
      if count == 4:
        return True
  return False


def diagonal_r_check(col, row, player):
  for index in range(0, 6):
    if row == 0 or col == 0:
      break
    row -= 1
    col -= 1

  count = 0

  for index in range(0, 6):
    piece = gameboard[row][col]

    if piece == "  " or gameboard[row][col] != player:
      count = 0
    elif player == piece:
      count += 1
      if count == 4:
        return True

    row += 1
    col += 1
    if row == 6 or col == 7:
      break

  return False


def diagonal_L_check(col, row, player):
  for index in range(0, 6):
    if row == 0 or col == 6:
      break
    row -= 1
    col += 1

  count = 0
  for index in range(0, 6):
    piece = gameboard[row][col]

    if piece == "  " or gameboard[row][col] != player:
      count = 0
    elif player == piece:
      count += 1
      if count == 4:
        return True

    row += 1
    col -= 1
    if row == 6 or col == -1:
      break

  return False


gameboard = [[], [], [], [], [], []]
for row in range(0, len(gameboard)):
  for col in range(0, 7):
    gameboard[row].append("  ")

player1 = "🔴"

player2 = "🔵"
playerwon = player1
while True:

  os.system("clear")
  printgameboard(gameboard)
  row, col = playerturn(gameboard, player1)
  won = False
  won = Horizontal_check(row, player1)
  if won == False:
    won = Vertical_check(col, player1)
  if won == False:
    won = diagonal_r_check(col, row, player1)
  if won == False:
    won = diagonal_L_check(col, row, player1)
  if won == True:
    playerwon = player1
    break

  os.system("clear")
  printgameboard(gameboard)
  row, col = playerturn(gameboard, player2)
  won = Horizontal_check(row, player2)
  if won == False:
    won = Vertical_check(col, player2)
  if won == False:
    won = diagonal_r_check(col, row, player2)
  if won == False:
    won = diagonal_L_check(col, row, player2)
  if won == True:
    playerwon = player2
    break

  if is_board_full(gameboard):
    os.system("clear")
    printgameboard(gameboard)
    print("It's a draw!")
    break

os.system("clear")
printgameboard(gameboard)
print(f"oh great job {playerwon} haha")
