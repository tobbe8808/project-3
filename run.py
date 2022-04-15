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


def printGameBoard():  # makes the gameboard
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")


def modifyArray(num, turn):  # modifies gameboard
    board[(num-1)//3][(num-1) % 3] = turn
