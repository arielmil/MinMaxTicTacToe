from Min_Max_v1 import *
from random import randint

GameBoard = Board()

def selectSymbol(ComVsCom = False):
    symbol = None

    if not(ComVsCom):
        while symbol not in ["X", "O"]:
            symbol = input("Input desired symbol (X or O): ")
    else:
        randomValue = randint(0, 1)
        if randomValue == 0:
            symbol = "O"
        else:
            symbol = "X"
            
    return symbol

def startSymbol(ComVsCom = False):
    symbol = None

    if not(ComVsCom):
        while symbol not in ["X", "O"]:
            symbol = input("Input start symbol (X or O): ")
    else:
        randomValue = randint(0, 1)
        if randomValue == 0:
            symbol = "O"
        else:
            symbol = "X"
                
    return symbol

def humanTurn(symbol):
    
    row = int(input("\nInput desired row: "))
    col = int(input("Input desired col: "))

    pos = {"row": row, "col": col}
    
    GameBoard.makeMove(pos, symbol, False)

def ComTurn(symbol, turn, firstPlayer = False):
    emptyPositions = GameBoard.getEmptyPositions()

    ComBoard = GameBoard.deepCopyBoard()

    bestMove = None
    bestEval = -100000

    depth = 10 - turn
    
    for emptyPosition in emptyPositions:

        ComBoard.makeMove(emptyPosition, symbol)
        evaluation = minMaxSearch(symbol, firstPlayer, depth, ComBoard)
        ComBoard.unMakeMove(emptyPosition, symbol)

        if evaluation >= bestEval:
            bestEval = evaluation
            bestMove = emptyPosition
    
    GameBoard.makeMove(bestMove, symbol)

def gameLoop(ComVsCom = False):
    
    humanSymbol = selectSymbol(ComVsCom)
    currentPlayer = startSymbol(ComVsCom)
    
    if humanSymbol == "X":
        ComSymbol = "O"
    else:
        ComSymbol = "X"

    if currentPlayer != humanSymbol:
        ComStarts = True
    else:
        ComStarts = False
    
    i = 0
    while (i < 9):
        
        if currentPlayer == humanSymbol:
            if not(ComVsCom):
                humanTurn(humanSymbol)
            else:
                ComTurn(humanSymbol, i, not(ComStarts))
                
            currentPlayer = ComSymbol
        else:
            ComTurn(ComSymbol, i, ComStarts)
            currentPlayer = humanSymbol

        print()
        GameBoard.printBoard()
        
        winner = GameBoard.checkWinner()
        
        if winner != -1:
            print("\n%s"% Board.symbolToInt(winner))
            return

        i += 1

gameLoop(True)
