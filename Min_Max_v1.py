from Tic_Tac_Toe_Board import *

def minMaxSearch(maxSymbol, maxTurn, depth, board):
    if depth == 0:
        return staticEvaluation(board)

    emptyPositions = board.getEmptyPositions()
    winner = board.checkWinner()

    if maxSymbol == "X":
        minSymbol = "O"
    else:
        minSymbol = "X"

    #Max plays    
    if (maxTurn):
        maxSymbolInInt = Board.symbolToInt(maxSymbol)
        
        maxEval = -2
        
        if winner == Board.symbolToInt(maxSymbol):
            return 1
        elif winner != -1:
            return -1
        
        for emptyPosition in emptyPositions:
            board.makeMove(emptyPosition, maxSymbol)
            evaluation = minMaxSearch(maxSymbol, False, depth - 1, board)
            maxEval = max(maxEval, evaluation)
            board.unMakeMove(emptyPosition)
            
        return maxEval

    #Min plays
    else:
        minSymbolInInt = Board.symbolToInt(minSymbol)
        minEval = 2

        if winner == minSymbolInInt:
            return -1
        elif winner != -1:
            return 1
        
        for emptyPosition in emptyPositions:
            board.makeMove(emptyPosition, minSymbol)
            evaluation = minMaxSearch(maxSymbol, True, depth - 1, board)
            minEval = min(minEval, evaluation)
            board.unMakeMove(emptyPosition)
            
        return minEval

def staticEvaluation(board):
    gameOver = board.checkWinner()

    #Victory
    if (gameOver == 1):
        return 1

    #Loose
    elif gameOver == 0:
        return -1

    #Draw or unfinished
    return 0

def test_MinMaxSearch():
    board = Board()
    print(minMaxSearch("1", 9, board))
