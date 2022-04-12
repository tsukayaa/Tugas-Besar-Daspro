board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
gameRunning = True
winner = None


#Print Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")

#Masukkan Input Player
def inputPlayer(board):
    t = bool(1)
    while t :
        x = int(input("Pilih spot yang ingin dipilih"))
        if(x >= 1 and x <= 9 and board[x - 1] == "-"):
            board[x - 1] = currentPlayer
            t = 0
        else:
            print("Sepertinya spot tersebut telah diambil")
            printBoard(board)

#Check Menang atau Seri
def checkHorizontal(board):
    global gameRunning
    global winner
    if(board[0] == board[1] == board[2] and board[0] != "-"):
        gameRunning = False
        winner = board[0]
        return True
    elif (board[3] == board[4] == board[5] and board[3] != "-"):
        gameRunning = False
        winner = board[3]
        return True
    elif (board[6] == board[7] == board[8] and board[6] != "-"):
        gameRunning = False
        winner = board[6]
        return True

def checkVertikal(board):
    global gameRunning
    global winner
    if(board[0] == board[3] == board[6] and board[0] != "-"):
        gameRunning = False
        winner = board[0]
        return True
    elif (board[1] == board[4] == board[7] and board[1] != "-"):
        gameRunning = False
        winner = board[1]
        return True
    elif (board[2] == board[5] == board[8] and board[2] != "-"):
        gameRunning = False
        winner = board[2]
        return True

def checkDiagonal(board):
    global gameRunning
    global winner
    if(board[0] == board[4] == board[8] and board[0] != "-"):
        gameRunning = False
        winner = board[0]
        return True
    elif (board[2] == board[4] == board[6] and board[4] != "-"):
        gameRunning = False
        winner = board[4]
        return True

def checkWin(board):
    if(checkDiagonal(board) or checkVertikal(board) or checkHorizontal(board)):
        print("Pemenangnya adalah ", winner)

def checkSeri(board):
    global gameRunning
    if("-" not in board):
        printBoard(board)
        print("Wah sepertinya pertandingan berakhir seri")
        gameRunning = False
#Tukar Player
def switchPlayer():
    global currentPlayer
    if (currentPlayer == "X"):
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#Game Berjalan

while gameRunning:
    printBoard(board)
    inputPlayer(board)
    checkWin(board)
    checkSeri(board)
    switchPlayer()
