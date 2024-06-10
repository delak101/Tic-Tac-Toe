import tkinter as tk, random as r, glob as g

# tinker to create the gui
root = tk.Tk()
root.title("Tic Tac Toe")

board = [["" for i in range(3)] for j in range(3)]
buttons = []
# random to implement computers random moves
# glob to handle file patterns

# Initialize the Main Window

# Create the main window using Tkinter.
# Set the title and size of the window.
# Create the Game Board

# Use a 2D list to represent the game board.
# Initialize the board with empty strings or spaces.
# Define the GUI Elements

# Create buttons for each cell in the 3x3 grid.
# Add labels to display the game status (e.g., whose turn it is, game over).
# Handle User Input
 
# Define a function to handle button clicks.
# Update the board and the button text when a cell is clicked.
# Check for a win or a draw after each move.
# Implement AI Moves
 
# Use the random module to generate random moves for the computer.
# Ensure the computer places its move in an empty cell.
# Check for Win/Draw

# Define functions to check rows, columns, and diagonals for a win.
# Check for a draw if all cells are filled and there is no winner.
# Restart the Game
 
# Add a button or functionality to reset the game board and start a new game.
