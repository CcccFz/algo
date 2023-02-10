#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check, col_check, block_check = [0]*9, [0]*9, [0]*9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                x = 1<<(ord(board[i][j])-ord('1'))
                if row_check[i] & x:
                    return False
                row_check[i] |= x
                if col_check[j] & x:
                    return False
                col_check[j] |= x
                if block_check[j//3*3+i//3] & x:
                    return False
                block_check[j//3*3+i//3] |= x
        return True
# @lc code=end
s = Solution()

# true
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

# false
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))