import random


print("----------------------")  # welcome message
print("Welcome to tobbes Tic Tac Toe game")
print("The game is played on a grid that's 3 squares by 3 squares.")
print("Connect three to win the game up, down, across, or diagonally")
print("if board is full its a draw")


print("----------------------")

player = input("Enter Player name: ")
print("Hello", player + "!")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3
