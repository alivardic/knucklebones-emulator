import random
import time,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.001)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.001)
  value = input()  
  return value

def display_board(board,com_b, col_sum):
    print("   YOU     |  COMPUTER")
    print(f"{board[0]} | {board[1]} | {board[2]}     {com_b[0]} | {com_b[1]} | {com_b[2]}")
    print("--+---+--  |  --+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}     {com_b[3]} | {com_b[4]} | {com_b[5]}")
    print("--+---+--  |  --+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}     {com_b[6]} | {com_b[7]} | {com_b[8]}")
    print("--+---+--  |  --+---+--")
    print("= | = | =     = | = | = ")
    print(f"{col_sum[0]} | {col_sum[1]} | {col_sum[2]}  |  {col_sum[3]} | {col_sum[4]} | {col_sum[5]}")


def sum_calc(array, position, nums):
    final_position_eval = array[position]
    for value in nums:
        if array[position] == array[value]:
            final_position_eval += array[position]
    return final_position_eval
    
def col_sums(board, com_b, col_sum):
    col_sum[0] = (sum_calc(board, 0, [3,6])) + (sum_calc(board, 3, [0,6])) + (sum_calc(board, 6, [0,3]))
    col_sum[1] = (sum_calc(board, 1, [4,7])) + (sum_calc(board, 4, [1,7])) + (sum_calc(board, 7, [1,4]))
    col_sum[2] = (sum_calc(board, 2, [5,8])) + (sum_calc(board, 5, [2,8])) + (sum_calc(board, 8, [2,5]))

    col_sum[3] = (sum_calc(com_b, 0, [3,6])) + (sum_calc(com_b, 3, [0,6])) + (sum_calc(com_b, 6, [0,3]))
    col_sum[4] = (sum_calc(com_b, 1, [4,7])) + (sum_calc(com_b, 4, [1,7])) + (sum_calc(com_b, 7, [1,4]))
    col_sum[5] = (sum_calc(com_b, 2, [5,8])) + (sum_calc(com_b, 5, [2,8])) + (sum_calc(com_b, 8, [2,5]))

    return col_sum


def who_winner(col_sum):
    if col_sum[0]+col_sum[1]+col_sum[2] > col_sum[3]+col_sum[4]+col_sum[5]:
        return "You are the Winner!"
    if col_sum[0]+col_sum[1]+col_sum[2] == col_sum[3]+col_sum[4]+col_sum[5]:
        return "Its a tie :O"
    else:
        return "The computer is the Winner :("

def is_board_full(board):
    # check if *all* items in the board list are not equal to a 0 character:
        return all(cell != 0 for cell in board)


def check_col(same, differ, position, check_col):
    for value in check_col:
        if same[position] == differ[value]:
            differ[value] = 0
    return differ

def get_player_move(board, com_b):
    # ask player for board position
    needs_position = True
    dice_roll = random.randint(1,6)
    while needs_position:
        position = typingInput(f"Your dice rolled {dice_roll}. Where would you like to place your marker (1-9)?: ")

        # convert the input to int and subtract 1 (remember, Python is zero-indexed!)
        position = int(position) - 1

        # check if choice is valid.
        # (i.e. is it between 0 and 8 inclusive and board at that position is empty)
        if board[position] == 0 and 0 <= position <= 8:
            # put 'X' at the chosen position
            board[position] = dice_roll
            #Check opposing columns for same position value
            if position in [0,3,6]:
                com_b = check_col(board, com_b, position, [0,3,6])
            if position in [1,4,7]:
                com_b = check_col(board, com_b, position, [1,4,7])
            if position in [2,5,8]:
                com_b = check_col(board, com_b, position, [2,5,8])
            # Update flag
            needs_position = False

        # otherwise, print message to select a valid board position.
        else:
            print("Please enter a valid position.")
            
    # return board
    return board

def get_computer_move(com_b, board):
    # random move function
    dice_roll = random.randint(1,6)

    # original random move function
    needs_position = True
    while needs_position:
        position = random.randint(0, 8)
        if com_b[position] == 0:
            # update board with 'O'
            com_b[position] = dice_roll

            # Check Opposing Col
            if position in [0,3,6]:
                board = check_col(com_b, board, position, [0,3,6])
            if position in [1,4,7]:
                board = check_col(com_b, board, position, [1,4,7])
            if position in [2,5,8]:
                board = check_col(com_b, board, position, [2,5,8])

            # update flag
            needs_position = False

    # return board
    return com_b

def play_game():
    # create board
    board = [0 for _ in range(9)]
    com_b = [0 for _ in range(9)]
    col_sum = [0 for _ in range(9)]

    # create loop and variable
    continue_playing = True
    while continue_playing:
        # Human player always goes first 
        
        # Display the board to the player
        col_sums(board, com_b, col_sum)
        display_board(board,com_b,col_sum)

        # get position from player (helper functions!)
        board = get_player_move(board,com_b)


        if is_board_full(board):
            display_board(board,com_b,col_sum)
            print("------------------------------")
            print (f"Your Final Sum: {sum(board)}  |  Computer Final Sum: {sum(com_b)}")
            print(who_winner(col_sum))
            break

        # get computer move 
        com_b = get_computer_move(com_b, board)

        # check if com is the winner
        if is_board_full(com_b):
            display_board(board,com_b,col_sum)
            print("------------------------------")
            print (f"Your Final Sum: {sum(board)}  |  Computer Final Sum: {sum(com_b)}")
            print(who_winner(col_sum))
            break

game = True

rules = input("Do you know the rules? y/n: ")
if rules == "n":
    print("Players take turns rolling a single six-sided die and placing it on their side of the board.")
    print("Each player has their own 3x3 grid, and their score is the total of all the dice currently placed there.")
    print("When one player has filled all nine slots on their board, the game ends, and the player with the highest score wins.")
    print("\n")
    print("Each player's grid is divided into three columns. If a player has two or three dice showing the same number in a single column,")
    print("their values are added together and multiplied by the number of matches." + "\n")
    print("If a player places a die that matches one or more dice in their opponent's corresponding column, all of their opponent's matching dice are removed.") 
    print("This allows you to get rid of high-scoring dice, even doubles or triples, as long as you have somewhere for your matching die to go.")
    print("\n")
    time.sleep (5)

while game:
    play_game()
    play_again=typingInput("try again y/n?: ")
    if play_again == 'y':
        continue
    else:
        typingPrint("Thanks for playing!")
        game = False

 
















# Last edited: 3/25/24 7:22 PM