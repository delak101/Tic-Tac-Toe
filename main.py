import tkinter as tk, random as r, glob as g

# tinker to create the gui
frame = tk.Tk()
frame.title("Tic Tac Toe")
frame.geometry("500x500")

buttonTest1 = tk.Button(frame, text = "  ")
buttonTest2 = tk.Button(frame, text = "  ")
buttonTest3 = tk.Button(frame, text = "  ")
buttonTest4 = tk.Button(frame, text = "  ")
buttonTest5 = tk.Button(frame, text = "  ")
buttonTest6 = tk.Button(frame, text = "  ")
buttonTest7 = tk.Button(frame, text = "  ")
buttonTest8 = tk.Button(frame, text = "  ")
buttonTest9 = tk.Button(frame, text = "  ")
buttonTest1.pack(side="left")
buttonTest2.pack()
buttonTest3.pack(side="right")
buttonTest4.pack(side="left")
buttonTest5.pack()
buttonTest6.pack(side="right")
buttonTest7.pack(side="left")
buttonTest8.pack()
buttonTest9.pack(side="right")

#can you see me?

frame.mainloop()

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
