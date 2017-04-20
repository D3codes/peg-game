import board
import console
import window

move = []
console.clearScreen()
window.drawBoard()
while True:
    move = console.getMove()
    console.clearScreen()
    if not board.move(move[0], move[1]):
        console.invalidMoveMessage()
    window.drawBoard()
    if board.wonGame():
        console.winMessage()
        if console.playAgain():
            board.setBoard()
        else:
            break
    if not board.movePossible():
        console.gameOverMessage()
        if console.playAgain():
            board.setBoard
        else:
            break
