#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isOk(row, col):
            for i in range(row):
                if board[i] == col:
                    return False
                if row-i == abs(board[i]-col):
                    return False
            return True

        def n_queens(row):
            if row == n:
                ans_board = []
                for i in range(n):
                    ans_row[board[i]] = 'Q'
                    ans_board.append(''.join(ans_row))
                    ans_row[board[i]] = '.'
                ans.append(ans_board)
                return
            for col in range(n):
                if isOk(row, col):
                    board[row] = col
                    n_queens(row+1)
            
        ans = []
        ans_row = ['.'] * n
        board = [0] * n
        n_queens(0)
        return ans
# @lc code=end
s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(1))
