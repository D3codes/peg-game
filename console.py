import board

def getSymbol(peg):
    if peg:
        return '|'
    return 'o'

def println(message):
    print(message)

def printBoard():
    print("    " + getSymbol(board.isOccupied(0)) + "             0")
    print("   " + getSymbol(board.isOccupied(1)) + " " + getSymbol(board.isOccupied(2)) + "           1  2")
    print("  " + getSymbol(board.isOccupied(3)) + " " + getSymbol(board.isOccupied(4)) + " " + getSymbol(board.isOccupied(5)) + "         3  4  5")
    print(" " + getSymbol(board.isOccupied(6)) + " " + getSymbol(board.isOccupied(7)) + " " + getSymbol(board.isOccupied(8)) + " " + getSymbol(board.isOccupied(9)) + "       6  7  8  9")
    print(getSymbol(board.isOccupied(10)) + " " + getSymbol(board.isOccupied(11)) + " " + getSymbol(board.isOccupied(12)) + " " + getSymbol(board.isOccupied(13)) + " " + getSymbol(board.isOccupied(14)) + "    10 11 12 13 14")

def getMove():
    move = [None] * 2
    move[0] = int(input("Which peg do you want to move? (0-14): "))
    move[1] = int(input("Where do you want to move it? (0-14): "))
    return move

def invalidMoveMessage():
    print("Invalid Move")

def clearScreen():
    print("\x1b[2J\x1b[H")

def winMessage():
    print("You Won!")

def gameOverMessage():
    print("Game Over")

def playAgain():
    again = input("Play Again? (y/n): ")[0]
    if again == 'y' or again == 'Y':
        return True
    return False
