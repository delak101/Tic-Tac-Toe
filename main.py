import tkinter as tk
import random as rand

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("511x511")

# Scores
player_score = 0
computer_score = 0

# Function to handle player's move
def player_move(button):
    global player_score
    button.config(text="X", state=tk.DISABLED, bg="light blue")
    if check_winner("X"):
        player_score += 1
        update_score()
        highlight_winner("X")
    else:
        computer_move()

# Function to handle computer's move
def computer_move():
    global computer_score
    empty_buttons = [button for button in [topL, topC, topR, midL, midC, midR, botL, botC, botR] if button.cget("text") == " "]
    if empty_buttons:
        button = rand.choice(empty_buttons)
        button.config(text="O", state=tk.DISABLED, bg="light green")
        if check_winner("O"):
            computer_score += 1
            update_score()
            highlight_winner("O")

# Function to check for a winner
def check_winner(player):
    lines = [
        [topL, topC, topR], [midL, midC, midR], [botL, botC, botR],  # horizontal
        [topL, midL, botL], [topC, midC, botC], [topR, midR, botR],  # vertical
        [topL, midC, botR], [topR, midC, botL]  # diagonal
    ]
    for line in lines:
        if all(button.cget("text") == player for button in line):
            return True
    return False

# Function to update score labels
def update_score():
    playerScore.config(text=f"Player: {player_score}")
    computerScore.config(text=f"PC: {computer_score}")

# Function to highlight the winning combination
def highlight_winner(player):
    lines = [
        [topL, topC, topR], [midL, midC, midR], [botL, botC, botR],  # horizontal
        [topL, midL, botL], [topC, midC, botC], [topR, midR, botR],  # vertical
        [topL, midC, botR], [topR, midC, botL]  # diagonal
    ]
    for line in lines:
        if all(button.cget("text") == player for button in line):
            for button in line:
                button.config(bg="yellow")


# Function to reset the game
def restart_game():
    global player_score, computer_score
    update_score()
    for button in [topL, topC, topR, midL, midC, midR, botL, botC, botR]:
        button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")

# Score labels
playerScore = tk.Label(root, text=f"Player: {player_score}")
computerScore = tk.Label(root, text=f"PC: {computer_score}")
playerScore.grid(row=0, column=2, sticky=tk.E)
computerScore.grid(row=0, column=2, sticky=tk.W)

# Restart button
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=1, column=2, sticky=tk.EW)

# Game buttons
topL = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(topL))
topC = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(topC))
topR = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(topR))
midL = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(midL))
midC = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(midC))
midR = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(midR))
botL = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(botL))
botC = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(botC))
botR = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6, command=lambda: player_move(botR))

topL.grid(row=2, column=1, sticky=tk.NSEW)
topC.grid(row=2, column=2, sticky=tk.NSEW)
topR.grid(row=2, column=3, sticky=tk.NSEW)
midL.grid(row=3, column=1, sticky=tk.NSEW)
midC.grid(row=3, column=2, sticky=tk.NSEW)
midR.grid(row=3, column=3, sticky=tk.NSEW)
botL.grid(row=4, column=1, sticky=tk.NSEW)
botC.grid(row=4, column=2, sticky=tk.NSEW)
botR.grid(row=4, column=3, sticky=tk.NSEW)

# Start the main loop
root.mainloop()