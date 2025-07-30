# Summarize - Knucklebones Emulator
Cult of the Lamb is a 2022 roguelike video game developed by Australian studio Massive Monster and published by Devolver Digital. The game follows the last lamb in the world as it makes a deal with a dark god to make a cult in its name in exchange for saving the lamb's life as it is sacrificed. Throughout the game, players have to juggle defeating enemy gods, gathering materials to upgrade their skills and base, all while keeping their ever-growing cult happy. 

However, cult management and boss fights are not the only tasks given to players throughout the game. Shortly after completling their beginning tasks, players are introduced to the minigame `Knucklebones`, a dice game of risk and reward. Players encounter multiple figures throughout the main game interested in facing off against the player at this game of chance with the potential to earn money, loyalty, or lose it all. 

While Knucklebones is an incredibly minor aspect of Cult of the Lamb and has little to no baring on the game itself as a whole. Knuclesbones is a fun way to destress and stretch some strategic muscles in a game more primarily focused on combat and resource management. 

This code seeks to emulate the mechanics of Knucklebones and replicate the gameplay outside of its the rougelike setting. 

## 🎲 Code Developement
### 🖥️ IDE Console
This code was originally developed to be an IDE console version of Knucklebones and an exercise in gamplay emmulation. The game is implemented as a procedural Python script using standard libraries (random, time, sys). The main components are:
| Function                                       | Purpose                                                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `typingPrint(text)` / `typingInput(text)`      | Simulates typewriter-style printing and input for a better console experience.                                                 |
| `display_board(board, com_b, col_sum)`         | Renders the current state of the player and computer boards, along with column sums.                                           |
| `sum_calc(array, position, nums)`              | Calculates the score contribution for a cell by checking for matching dice in a column.                                        |
| `col_sums(board, com_b, col_sum)`              | Updates the total column scores for both players using `sum_calc()`.                                                           |
| `who_winner(col_sum)`                          | Determines the winner by comparing the summed column scores.                                                                   |
| `is_board_full(board)`                         | Checks if a board is completely filled (no zeros remain).                                                                      |
| `check_col(same, differ, position, check_col)` | Removes matching dice from the opponent’s column when a die is placed.                                                         |
| `get_player_move(board, com_b)`                | Handles user input for rolling a die and selecting a valid position. It also applies the opponent column-removal mechanic.     |
| `get_computer_move(com_b, board)`              | Randomly selects a valid position for the computer’s die roll and applies the same column-removal mechanic.                    |
| `play_game()`                                  | Contains the main game loop: displaying the board, alternating turns, checking for game-over conditions, and printing results. |

The original IDE console version of this app can be run with the `summarize.py` using your IDE terminal. 

### 🌐 Streamlit Web App
While this emmulation was originally developed and completed to run as a IDE terminal app, adjustments were made to develop a Streamlit app version that would be easily shared on Github.

#### Major Script Differences
Input/ Output Handling:
| Original IDE Version                                     | Streamlit Version                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Used `typingInput()` and `input()` for text-based input. | Uses **Streamlit buttons** (`st.button`) for interaction.                      |
| Used `print()` to display the board.                     | Uses `st.text()`, `st.write()`, and columns to show the board in the browser.  |
| Animated typing effect with `typingPrint()`.             | No typing animation—Streamlit UI updates dynamically when buttons are pressed. |

Game State Management
| Original IDE Version                                                                    | Streamlit                                                                                                                                  |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Game state stored in **local variables** (`board`, `com_b`, etc.) inside `play_game()`. | Game state stored in **`st.session_state`**, so it **persists between button clicks** (Streamlit re-runs the script on every interaction). |
| A `while` loop runs the entire game until it ends.                                      | **No game loop.** The app **re-runs from the top** on every button click, using session state to remember progress.                        |

Player Interaction
| Original IDE Version                                                    | Streamlit                                                                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Dice is rolled inside `get_player_move()` before asking for a position. | Dice is rolled with a **"🎲 Roll Dice" button**. The roll is stored in `st.session_state.last_roll`. |
| User inputs a position number.                                          | The board is rendered as **grid buttons**, and the player clicks the square they want.               |

Other minor changes were made to the original IDE script to fit the needs of the Streamlit app, most of which can be summarized with the fact that the IDE version primarily depends on `for` and `while` loops, while the Streamlit app depends on session states to track computer and player moves.

## App Link ⌯⌲
The link to play the Streamlit Version of the emmulation can be found: Here [https://knucklebones-emulator.streamlit.app/]


