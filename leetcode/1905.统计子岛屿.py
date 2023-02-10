#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#
from typing import List
# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def in_area(i, j):
            return 0 <= i < len(grid2) and 0 <= j < len(grid2[0])

        def dfs(i, j):
            if not in_area(i, j) or grid2[i][j] == 0:
                return
            self.isSub &= grid1[i][j]
            grid2[i][j] = 0
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i+1, j)
            
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    self.isSub = 1
                    dfs(i, j)
                    if self.isSub:
                        ans += 1
        return ans
# @lc code=end
s = Solution()
# 3
print(s.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
# 2
print(s.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))