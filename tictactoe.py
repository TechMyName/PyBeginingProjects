# ----------------- Global Variables -----------------------
#Display the board, it's a list item.
board = ["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-"]

#Current player, always begins with X
current_player = 'X'

#Checks if the game is over 
game_is_on = True

#Tells us who is the winner 
winner = None

# ----------------- Functions -----------------------

def play_game():
  global winner

   #Display initial board
  display_board()

  while game_is_on:
    #handles player's turn
    handle_turn(current_player)

    # checks if the game is over
    check_if_game_over()

    #flips the player
    flip_player()

  # Print a winer or tie when the game is over  
  if winner == 'X' or winner == 'O':
    print(f"{winner} won the game")
  elif winner == None:
    print("It's a tie.")


    
def display_board():
  print('\n')
  print(f"{board[0]} | {board[1]} | {board[2]}    1 | 2 | 3")
  print(f"{board[3]} | {board[4]} | {board[5]}    4 | 5 | 6")
  print(f"{board[6]} | {board[7]} | {board[8]}    7 | 8 | 9")
  print('\n')

#To handle players turn and print the input provided by user. 
def handle_turn(player):

  print(f"{player}'s turn-")
  
  position = input("Enter your position (1-9): ")

  #To ensure user input is valied
  valid = False
  while not valid:
    
    #To ensure the value is only between 1 - 9. 
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      position = input("Wrong input, Enter your position (1-9): ")

    position = int(position) - 1

    #To ensure the input spot is available
    if board[position] == '-':
      valid = True
    else:
      print("You can't go there. Go again")

  #Put the game piece on the board
  board[position] = player

  #show the game board
  display_board()


#game over check, in 2 condition if someone wins, or ot's a tie
def check_if_game_over():
  check_winner()
  check_tie() 

def check_winner():
  global winner
  
  # check who wins the game out of 3 
  row_winner = check_row_winner()
  column_winner = check_column_winner()
  diagonal_winner = check_diagonal_winner()

  #whosoevers wins gets assigned to the winner variable
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

#functions returns row_winner as soon as there is a row win  
def check_row_winner():
  global game_is_on

  row1 = board[0] == board[1] == board[2] != '-'
  row2 = board[3] == board[4] == board[5] != '-'
  row3 = board[6] == board[7] == board[8] != '-'

  #if any row has a match, game is over
  if row1 or row2 or row3:
    game_is_on = False
  
  #return the row winner
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  else:
    return None

#functions returns column_winner as soon as there is a column win
def check_column_winner():
  global game_is_on

  column1 = board[0] == board[3] == board[6] != '-'
  column2 = board[1] == board[4] == board[7] != '-'
  column3 = board[2] == board[5] == board[8] != '-'

  #if any column has a match, game is over
  if column1 or column2 or column3:
    game_is_on = False
  
  #return the column winner
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  else:
    return None

#functions returns diagonal_winner as soon as there is a diagonal win
def check_diagonal_winner():
    global game_is_on

    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[6] == board[4] == board[2] != '-'

    #if any column has a match, game is over
    if diagonal1 or diagonal2:
        game_is_on = False
    
    #return the column winner
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    else:
        return None

def check_tie():
  global game_is_on

  if '-' not in board:
    game_is_on = False
    return True 
  else:
    return False

#Flip the player depending upon who is playing currently
def flip_player():
  global current_player

  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'

#start the game
play_game()