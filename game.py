import board
import console
import window

move = []
console.clearScreen()
while True:
    window.drawBoard(board.board)
    move = console.getMove()
    console.clearScreen()
    if not board.move(move[0], move[1]):
        console.invalidMoveMessage()
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
