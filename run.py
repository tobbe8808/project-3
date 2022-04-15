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


def checkForWinner(board):  # checking possible winner
    # X axis
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print(player, "winner")
        return "X"
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("O has won!")
        return "O"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print(player, "winner")
        return "X"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("O has won!")
        return "O"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print(player, "winner")
        return "X"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("O has won!")
        return "O"
    # Y axis
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(player, "winner")
        return "X"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("O has won!")
        return "O"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print(player, "winner")
        return "X"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("O has won!")
        return "O"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print(player, "winner")
        return "X"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("O has won!")
        return "O"
    # Cross wins
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print(player, "winner")
        return "X"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("O has won!")
        return "O"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print(player, "winner")
        return "X"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("O has won!")
        return "O"
    else:
        return "N"

leaveLoop = False
turnCounter = 0

while not leaveLoop:
    if turnCounter % 2 == 0:  # computers turn
        cpuChoice = random.choice(possibleNumbers)
        print("\nComputer's choice: ", cpuChoice)
        modifyArray(cpuChoice, "O")
        possibleNumbers.remove(cpuChoice)

    else:  # Player's turn.
        printGameBoard()
        while True:
            try:
                numberPicked = int(input("\nChoose a number [1-9]: "))
            except ValueError:
                print("That was not a valid number, please try again.")
                continue

            if numberPicked not in possibleNumbers:
                print("That board position is invalid, try again.")
                continue
            else:
                modifyArray(numberPicked, "X")
                possibleNumbers.remove(numberPicked)
                break

    turnCounter += 1

    winner = checkForWinner(board)  # checking if game ended with win or tie
    if winner != "N" or not possibleNumbers:
        print("Game over!")
        if not possibleNumbers:
            print("Tie")
        while True:
            ans = input("Play again? (y/n): ")
            if ans.lower() not in ("y", "n"):
                print('Please answer with "y" or "n".')
            else:
                break
        if ans == "n":
            leaveLoop = True
        else:  # Reseting the game
            possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            turnCounter = 0
