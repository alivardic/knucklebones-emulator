import streamlit as st
import random

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [0]*9
if "com_b" not in st.session_state:
    st.session_state.com_b = [0]*9
if "turn" not in st.session_state:
    st.session_state.turn = "player"  # player or computer
if "last_roll" not in st.session_state:
    st.session_state.last_roll = 0
if "col_sum" not in st.session_state:
    st.session_state.col_sum = [0]*6

# Helper functions
def sum_calc(array, position, nums):
    final_position_eval = array[position]
    for value in nums:
        if array[position] == array[value]:
            final_position_eval += array[position]
    return final_position_eval

def col_sums(board, com_b):
    col_sum = [0]*6
    col_sum[0] = (sum_calc(board, 0, [3,6])) + (sum_calc(board, 3, [0,6])) + (sum_calc(board, 6, [0,3]))
    col_sum[1] = (sum_calc(board, 1, [4,7])) + (sum_calc(board, 4, [1,7])) + (sum_calc(board, 7, [1,4]))
    col_sum[2] = (sum_calc(board, 2, [5,8])) + (sum_calc(board, 5, [2,8])) + (sum_calc(board, 8, [2,5]))
    col_sum[3] = (sum_calc(com_b, 0, [3,6])) + (sum_calc(com_b, 3, [0,6])) + (sum_calc(com_b, 6, [0,3]))
    col_sum[4] = (sum_calc(com_b, 1, [4,7])) + (sum_calc(com_b, 4, [1,7])) + (sum_calc(com_b, 7, [1,4]))
    col_sum[5] = (sum_calc(com_b, 2, [5,8])) + (sum_calc(com_b, 5, [2,8])) + (sum_calc(com_b, 8, [2,5]))
    return col_sum

def is_full(board):
    return all(x != 0 for x in board)

def check_col(same, differ, position, check_col_list):
    for value in check_col_list:
        if same[position] == differ[value]:
            differ[value] = 0
    return differ

def computer_move():
    dice_roll = random.randint(1,6)
    while True:
        pos = random.randint(0, 8)
        if st.session_state.com_b[pos] == 0:
            st.session_state.com_b[pos] = dice_roll
            if pos in [0,3,6]:
                st.session_state.board = check_col(st.session_state.com_b, st.session_state.board, pos, [0,3,6])
            if pos in [1,4,7]:
                st.session_state.board = check_col(st.session_state.com_b, st.session_state.board, pos, [1,4,7])
            if pos in [2,5,8]:
                st.session_state.board = check_col(st.session_state.com_b, st.session_state.board, pos, [2,5,8])
            break

def reset_game():
    st.session_state.board = [0]*9
    st.session_state.com_b = [0]*9
    st.session_state.turn = "player"
    st.session_state.last_roll = 0
    st.session_state.col_sum = [0]*6

# UI
st.title("Summarize - Knucklebones Emulator")

# Add a button to show rules if rules are not known
if st.button("📜 Show Rules"):
    st.info("""
    **How to Play:**

    Players take turns rolling a six-sided die and placing it on their own 3x3 board.  
    The game ends when one player has filled all 9 squares. The player with the highest total score wins.

    ### Scoring:
    - Your board is divided into 3 columns.  
    - If you have **two or three dice with the same value in a column**, their values are **added together and multiplied by the number of matches**.  
      (Example: Two 4s in one column = 4+4, then ×2 = 16 points)

    ### Attacking the Opponent:
    - If you place a die that **matches one or more dice in the opponent's same column**, all matching dice in that column are **removed** from their board.  
    - This can remove even high-scoring doubles or triples!

    **Goal:** Maximize your score while sabotaging your opponent!
    """)

st.write("### Current Boards")
col_sum = col_sums(st.session_state.board, st.session_state.com_b)
st.session_state.col_sum = col_sum

def render_board(board):
    return f"""
    {board[0]} | {board[1]} | {board[2]}  
    --+---+--  
    {board[3]} | {board[4]} | {board[5]}  
    --+---+--  
    {board[6]} | {board[7]} | {board[8]}
    """

c1, c2 = st.columns(2)
with c1:
    st.subheader("You")
    st.text(render_board(st.session_state.board))
    st.text(f"= {col_sum[0]}, {col_sum[1]}, {col_sum[2]}")
with c2:
    st.subheader("Computer")
    st.text(render_board(st.session_state.com_b))
    st.text(f"= {col_sum[3]}, {col_sum[4]}, {col_sum[5]}")

# Gameplay
if st.session_state.turn == "player":
    if st.button("🎲 Roll Dice"):
        st.session_state.last_roll = random.randint(1,6)

    if st.session_state.last_roll > 0:
        st.write(f"You rolled a **{st.session_state.last_roll}**. Click a square to place it.")
        for i in range(0, 9, 3):
            cols = st.columns(3)
            for j in range(3):
                idx = i+j
                if cols[j].button(f"Place {st.session_state.last_roll}", key=f"cell_{idx}"):
                    if st.session_state.board[idx] == 0:
                        st.session_state.board[idx] = st.session_state.last_roll
                        if idx in [0,3,6]:
                            st.session_state.com_b = check_col(st.session_state.board, st.session_state.com_b, idx, [0,3,6])
                        if idx in [1,4,7]:
                            st.session_state.com_b = check_col(st.session_state.board, st.session_state.com_b, idx, [1,4,7])
                        if idx in [2,5,8]:
                            st.session_state.com_b = check_col(st.session_state.board, st.session_state.com_b, idx, [2,5,8])
                        st.session_state.last_roll = 0
                        st.session_state.turn = "computer"

# Computer move
if st.session_state.turn == "computer" and not is_full(st.session_state.com_b):
    computer_move()
    st.session_state.turn = "player"

# Check game over
if is_full(st.session_state.board) or is_full(st.session_state.com_b):
    st.subheader("🏆 Game Over!")
    player_score = col_sum[0] + col_sum[1] + col_sum[2]
    computer_score = col_sum[3] + col_sum[4] + col_sum[5]

    st.write(f"Your Final Sum: {player_score}")    
    st.write(f"Computer Final Sum: {computer_score}")

    if sum(st.session_state.board) > sum(st.session_state.com_b):
        st.success("🎉 You win!")
    elif sum(st.session_state.board) < sum(st.session_state.com_b):
        st.error("💻 Computer wins!")
    else:
        st.info("🤝 It's a tie!")

    if st.button("🔄 Play Again"):
        reset_game()
