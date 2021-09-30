import copy

class Board():
    def __init__(self):       
        self.board = []
        self.rows, self.cols = (3, 3)
        
        self.x = 1
        self.O = 0
        self.none = -1
        
        self.createBoard()

    def posIsValid(self, pos):
        (row, col) = (pos["row"], pos["col"])

        if (row >= 0 and row <= 2 and col >= 0 and col <= 2):
            return True
        return False
        
    def createBoard(self):
        self.board = [[-1 for i in range(self.rows)] for j in range(self.cols)]
        
    def checkWinner(self):
        winner = False
        i, j = (0, 0)
        
        rows = cols = [0,1,2]
                
        for row in rows:
            pos = {"row": row}
            
            horizontalWin = self.horizontalWin(pos)
            
            if (horizontalWin == 1):
                return 1
            elif (horizontalWin == 0):
                return 0

        for col in cols:
            pos = {"col": col}

            verticalWin = self.verticalWin(pos)

            if (self.verticalWin(pos) == 1):
                return 1
            elif (horizontalWin == 0):
                return 0
            
        diagonalURDLWin = self.diagonalURDLWin()
        diagonalULDRWin = self.diagonalULDRWin()
        
        if (diagonalURDLWin == 1 or diagonalULDRWin == 1):
            return 1
        elif (diagonalURDLWin == 0 or diagonalULDRWin == 0):
            return 0
    
        return -1

    def diagonalULDRWin(self):
        board = self.board
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == "X"):
            return 1
        elif (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == "O"):
            return 0
        return -1

    def diagonalURDLWin(self):
        board = self.board
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == "X"):
            return 1
        elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == "O"):
            return 0
        return -1

    def verticalWin(self, pos):
        board = self.board
        col = pos["col"]
        
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == "X"):
            return 1
        elif (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == "O"):
            return 0
        return -1

    def horizontalWin(self, pos):
        board = self.board
        row = pos["row"]
        
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][2] == "X"):
            return 1
        elif (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][2] == "O"):
            return 0
        return -1

    def copyBoard(self, board):
        self.board = board
        
    def deepCopyBoard(self):
        board = copy.deepcopy(self)
        return board


    #Ver e concertar
    def potentialWins(self, symbol, pos):
        potentialWins = 0
        
        (row, col) = (pos["row"], pos["col"])
        
        if (self.board[row][col] == symbol):
            if (row, col) in [(0, 0), (2, 2)]:
                potentialWins = diagonalULDRWin(symbol)
            elif (row, col) in [(2, 0), (0, 2)]:
                potentialWins = diagonalURDLWin(symbol)
            elif (row, col) == (1 ,1):
                potentialWins = diagonalULDRWin(symbol) + diagonalURDLWin(symbol)

            potentialWins = potentialWins + verticalWins(symbol, pos) + horizontalWins(symbol, pos)
            
        return potentialWins
        
    def getEmptyPositions(self):
    	emptyPositions = []
    	
    	i = 0
    	j = 0
    	
    	for row in self.board:
    		for pos in row:
    			if pos == -1:
    				emptyPositions.append({"row": i, "col": j})
    			j += 1
    		i += 1
    		j = 0

    	return emptyPositions

    def makeMove(self, pos, symbol, comPlays=True):
        if comPlays:
            self.board[pos["row"]][pos["col"]] = symbol
        else:
            if self.posIsValid(pos):
                self.board[pos["row"]][pos["col"]] = symbol
            else:
                return -1
        return symbol

    def unMakeMove(self, pos, comPlays=True):
        if comPlays:
            self.board[pos["row"]][pos["col"]] = -1

        else:
            if self.posIsValid(pos):
                self.board[pos["row"]][pos["col"]] = -1
            else:
                return -1
        return 1

    def symbolToInt(symbol):
        if symbol == "X":
            return 1
        else:
            return 0
        
    def printBoard(self):
        for row in self.board:
            print(row)
            

def testCheckWinner():
    board = Board()
    
    boardX = [[-1 for i in range(board.rows)] for j in range(board.cols)]
    boardO = [[-1 for i in range(board.rows)] for j in range(board.cols)]
    
    boardsX = []
    boardsO = []
    
    for i in range(8):
        boardsX.append(copy.deepcopy(boardX))
        boardsO.append(copy.deepcopy(boardO))

    for i in range(3):
        boardsX[i][i][0] = boardsX[i][i][1] = boardsX[i][i][2] = 1
        boardsO[i][i][0] = boardsO[i][i][1] = boardsO[i][i][2] = 0

    for i in range(3):
        boardsX[i + 3][0][i] = boardsX[i + 3][1][i] = boardsX[i + 3][2][i] = 1
        boardsO[i + 3][0][i] = boardsO[i + 3][1][i] = boardsO[i + 3][2][i] = 0

    i = i + 3
    
    boardsX[i + 1][0][0] = boardsX[i + 1][1][1] = boardsX[i + 1][2][2] = 1
    boardsO[i + 1][0][0] = boardsO[i + 1][1][1] = boardsO[i + 1][2][2] = 0
    
    boardsX[i + 2][0][2] = boardsX[i + 2][1][1] = boardsX[i + 2][2][0] = 1
    boardsO[i + 2][0][2] = boardsO[i + 2][1][1] = boardsO[i + 2][2][0] = 0

    for boardX in boardsX:
        board.copyBoard(boardX)

        i = 0
        for row in boardX:
            print("%d: " %i, row)
            i = i + 1
            
        print("winner's symbol:", board.checkWinner(board.x), "\n\n")

    for boardO in boardsO:
        board.copyBoard(boardO)

        i = 0
        for row in boardO:
            print("%d: " %i, row)
            i = i + 1
            
        print("winner's symbol:", board.checkWinner(board.O), "\n\n")
