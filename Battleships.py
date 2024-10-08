from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board[0]) - 1)

turn = 4
while turn>0:
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print_board(board)
      turn-=1

print("Game Over ")
print(ship_row, ship_row)
