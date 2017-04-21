board = [None] * 15

def setBoard():
    for i in range(0,15):
        board[i] = True
    board[0] = False

def movePossible():
    for i in range(0,15):
        for j in range(0,15):
            if canMove(i,j):
                return True
    return False

def wonGame():
    if pegsRemaining() > 1:
        return False
    return True

def pegsRemaining():
    pegs = 0
    for i in range(0,15):
        if board[i]:
            pegs+=1
    return pegs

def isOccupied(index):
    if index >= 0 and index <= 14:
        return board[index]
    return False

def middle(start, end):
    if start == 0:
        if end == 3:
            return 1
        if end == 5:
            return 2

    if start == 1:
        if end == 6:
            return 3
        if end == 8:
            return 4

    if start == 2:
        if end == 7:
            return 4
        if end == 9:
            return 5

    if start == 3:
        if end == 0:
            return 1
        if end == 5:
            return 4
        if end == 10:
            return 6
        if end == 12:
            return 7

    if start == 4:
        if end == 11:
            return 7
        if end == 13:
            return 8

    if start == 5:
        if end == 0:
            return 2
        if end == 3:
            return 4
        if end == 12:
            return 8
        if end == 14:
            return 9

    if start == 6:
        if end == 1:
            return 3
        if end == 8:
            return 7

    if start == 7:
        if end == 2:
            return 4
        if end == 9:
            return 8

    if start == 8:
        if end == 1:
            return 4
        if end == 6:
            return 7

    if start == 9:
        if end == 2:
            return 5
        if end == 7:
            return 8

    if start == 10:
        if end == 3:
            return 6
        if end == 12:
            return 11

    if start == 11:
        if end == 4:
            return 7
        if end == 13:
            return 12

    if start == 12:
        if end == 5:
            return 8
        if end == 3:
            return 7
        if end == 10:
            return 11
        if end == 14:
            return 13

    if start == 13:
        if end == 4:
            return 8
        if end == 11:
            return 12

    if start == 14:
        if end == 5:
            return 9
        if end == 12:
            return 13
    return -1;

def canMove(start, end):
    if start < 0 or start > 14:
        return False
    if end <0 or end > 14:
        return False

    if not board[start] or board[end]:
        return False
    mid = middle(start, end)
    if mid == -1:
        return False
    return board[mid]

def move(start, end):
    if not canMove(start, end):
        return False
    board[start] = False
    board[end] = True
    board[middle(start, end)] = False
    return True

setBoard()
