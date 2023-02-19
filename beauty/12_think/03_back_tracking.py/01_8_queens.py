SIZE = 8
board = [0] * SIZE
total = 0

def _8_queens(row):
    def isOk(row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if row-i == abs(board[i]-col):
                return False
        return True

    if row == SIZE:
        print(board)
        global total
        total += 1
        return
    for col in range(SIZE):
        if isOk(row, col):
            board[row] = col
            _8_queens(row+1)

_8_queens(0)
print(total)