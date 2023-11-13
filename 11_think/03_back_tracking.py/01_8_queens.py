SIZE = 8
board = [0] * SIZE
total = 0

def _8_queens(row):
    def is_ok(row, col):
        for i in range(row):
            if board[i] == col or row-i == abs(col-board[i]):
                return False
        return True
    if row == SIZE:
        global total
        total += 1
        print(board)
        return
    for col in range(SIZE):
        if is_ok(row, col):
            board[row] = col
            _8_queens(row+1)

_8_queens(0)
print(total)