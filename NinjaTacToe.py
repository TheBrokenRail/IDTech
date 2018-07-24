import random

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
currentPlayer = 1
playerTwoAI = False

def drawPoint(x, y):
    global board
    if board[x][y] == 0:
        return " "
    elif board[x][y] == 1:
        return "X"
    elif board[x][y] == 2:
        return "O"

def drawBoard():
    print("    1   2   3  ")
    print("  -------------")
    print("1 | " + drawPoint(0, 0) + " | " + drawPoint(1, 0) + " | " + drawPoint(2, 0) + " |")
    print("  -------------")
    print("2 | " + drawPoint(0, 1) + " | " + drawPoint(1, 1) + " | " + drawPoint(2, 1) + " |")
    print("  -------------")
    print("3 | " + drawPoint(0, 2) + " | " + drawPoint(1, 2) + " | " + drawPoint(2, 2) + " |")
    print("  -------------")

def addPoint(x, y, player):
    global board
    board[x][y] = player

def getPoint(x, y):
    global board
    if -1 < x < 3 and -1 < y < 3:
        return board[x][y]
    else:
        return 0

def randomPoint():
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    if getPoint(x, y) == 0:
        print("Column: " + str(x))
        print("Row: " + str(y))
        return [str(x), str(y)]
    else:
        return randomPoint()

def makeMove(player):
    if player == 2 and playerTwoAI:
        point = randomPoint()
        x = point[0]
        y = point[1]
    else:
        x = input("Column: ")
        y = input("Row: ")
    try:
        if 0 < int(y) < 4 and 0 < int(x) < 4:
            if getPoint(int(x) - 1, int(y) - 1) == 0:
                addPoint(int(x) - 1, int(y) - 1, player)
            else:
                print("Spot Taken!")
                makeMove(player)
        else:
            print("Invalid Position!")
            makeMove(player)
    except ValueError:
        print("Invalid Position!")
        makeMove(player)

def checkPoint(x, y, player):
    if getPoint(x, y - 1) == player and getPoint(x, y - 2) == player:
        return True
    elif getPoint(x, y + 1) == player and getPoint(x, y + 2) == player:
        return True
    elif getPoint(x, y + 1) == player and getPoint(x, y - 1) == player:
        return True
    elif getPoint(x + 1, y) == player and getPoint(x + 2, y) == player:
        return True
    elif getPoint(x - 1, y) == player and getPoint(x + 1, y) == player:
        return True
    elif getPoint(x - 1, y) == player and getPoint(x - 2, y) == player:
        return True
    elif getPoint(x + 1, y - 1) == player and getPoint(x + 2, y - 2) == player:
        return True
    elif getPoint(x - 1, y + 1) == player and getPoint(x + 1, y - 1) == player:
        return True
    elif getPoint(x - 1, y + 1) == player and getPoint(x - 2, y + 2) == player:
        return True
    elif getPoint(x + 1, y + 1) == player and getPoint(x + 2, y + 2) == player:
        return True
    elif getPoint(x - 1, y - 1) == player and getPoint(x + 1, y + 1) == player:
        return True
    elif getPoint(x - 1, y - 1) == player and getPoint(x - 2, y - 2) == player:
        return True
    else:
        return False

def detectWin():
    for x in range(0, 2):
        for y in range(0, 2):
            if getPoint(x, y) != 0:
                if checkPoint(x, y, getPoint(x, y)):
                    return getPoint(x, y)
    return 0

def setAI():
    global playerTwoAI
    defaultAI = input("Enter If Player 2 is an AI (False): ")
    if defaultAI == "":
        playerTwoAI = False
    elif defaultAI.lower() == "false":
        playerTwoAI = False
    elif defaultAI.lower() == "true":
        playerTwoAI = True
    elif defaultAI.lower() == "no":
        playerTwoAI = False
    elif defaultAI.lower() == "yes":
        playerTwoAI = True
    elif defaultAI.lower() == "n":
        playerTwoAI = False
    elif defaultAI.lower() == "y":
        playerTwoAI = True
    elif defaultAI.lower() == "0":
        playerTwoAI = False
    elif defaultAI.lower() == "1":
        playerTwoAI = True
    else:
        print("Invalid Value!")
        setAI()

print("NinjaTacToe By Connor Nolan!\n")
setAI()
print()

while not detectWin():
    print("Player " + str(currentPlayer) + "'s Turn!\n")
    drawBoard()
    makeMove(currentPlayer)
    print()
    if currentPlayer == 1:
        currentPlayer = 2
    elif currentPlayer == 2:
        currentPlayer = 1

drawBoard()
print("Player " + str(detectWin()) + " Won!")