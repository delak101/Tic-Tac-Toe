import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("310x400")

# Scores
player_score = 0
computer_score = 0

# Create a list to keep track of the board state
board = [" " for _ in range(9)]

# Function to handle player's move
def player_move(idx):
    global player_score
    if board[idx] == " ":
        board[idx] = "X"
        buttons[idx].config(text="X", state=tk.DISABLED, bg="light blue")
        if check_winner(board, "X"):
            player_score += 1
            update_score()
            highlight_winner("X")
            disable_buttons()
        else:
            computer_move()

# Function to handle computer's move
def computer_move():
    global computer_score
    empty_cells = [i for i, value in enumerate(board) if value == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
        buttons[move].config(text="O", state=tk.DISABLED, bg="light green")
        if check_winner(board, "O"):
            computer_score += 1
            update_score()
            highlight_winner("O")
            disable_buttons()

# Function to check for a winner
def check_winner(b, player):
    # Winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False

# Function to update score
def update_score():
    playerScore.config(text=f"Player: {player_score}")
    computerScore.config(text=f"PC: {computer_score}")

# Function to highlight the winning combination
def highlight_winner(player):
    for idx in range(9):
        if board[idx] == player:
            buttons[idx].config(bg="yellow")

# Function to disable all buttons after a win
def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Function to reset the game board and scores
def restart_game():
    global board, player_score, computer_score
    board = [" " for _ in range(9)]
    player_score = 0
    computer_score = 0
    update_score()
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")

# Function to reset only the game board
def play_again():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")

# Score display
playerScore = tk.Label(root, text=f"Player: {player_score}")
playerScore.grid(row=0, column=1, sticky=tk.E)
computerScore = tk.Label(root, text=f"PC: {computer_score}")
computerScore.grid(row=0, column=1, sticky=tk.W)

# Restart button
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=1, column=2, sticky=tk.EW)

# Play Again button
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=1, column=0, sticky=tk.EW)

# Buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6)
    button.grid(row=(i // 3) + 2, column=i % 3, sticky=tk.NSEW)
    button.config(command=lambda idx=i: player_move(idx))
    buttons.append(button)

# Window init
root.mainloop()
