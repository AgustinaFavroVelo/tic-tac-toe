import random

#STEP 1: create a board
board= ["-", "-","-",
        "-", "-","-",
        "-", "-","-"]

currentPlayer= "X"
winner= None
gameRunning= True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#STEP 2: player input
def playerInput(board):
    inp = int(input ("ingrese un numero entre 1-9: "))
    #check of the number is valid (bet 1 and 9) and if the index in the board (number-1)is free space
    if (inp >= 1 and inp <=9) and ( board [inp-1] == "-"):
        board[inp-1] = currentPlayer
    else:
        print("Oops. Ese espacio ya está ocupado")

#STEP 3: Check for win or tie, horizontal (column) or vertical(row)

#GANAR EN HORIZONTAL
def checkColumn(board):
    global winner
    if board[0] == board[1] and board[1] == board[2] and board[1] != "-":
        winner = board[2] #or 1, or cero, it's the same
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[4] != "-":
        winner = board[3] 
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[7] != "-":
        winner = board[6] 
        return True
    
#GANAR EN VERTICAL
def checkRow(board):
    global winner
    if board[0] == board[3] and board[3] == board[6] and board[3] != "-":
        winner = board[3] 
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[4] != "-":
        winner = board[4] 
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[5] != "-":
        winner = board[5] 
        return True
    
#GANAR EN DIAGONAL
def checkDiag(board):
    global winner
    if board[0] == board [4] and board[4] == board[8] and board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] and board [4] == board[6] and board[6] != "-":
        winner= board[2]
        return True
    
#CHEQUEAR WINNER
def checkWin(board):
    global gameRunning
    if checkColumn(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

#EMPATE
def checkTie(board):
    global gameRunning
    if "-" not in board:  #if all positions are taken and there is not any winner, then, there is a tie
        printBoard(board)
        print("Empate!")
        gameRunning = False

#SWITCH PLAYER
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":  #si el current player es x, entonces el que sigue es o
        currentPlayer = "O"
    # elif currentPlayer == "O":
    #     currentPlayer == "X"
    else:
        currentPlayer = "X"
#COMPUTER 
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#CHECK FOR WIN OR TIE AGAIN

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)