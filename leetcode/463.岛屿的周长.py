#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
from typing import List
# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def in_area(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i, j):
            if not in_area(i, j) or grid[i][j] == 0:
                return 1
            if grid[i][j] == 2:
                return 0
            grid[i][j] = 2
            return dfs(i,j-1)+dfs(i,j+1)+dfs(i-1,j)+dfs(i+1,j)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return ans
# @lc code=end
s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(s.islandPerimeter([[1]]))
print(s.islandPerimeter([[1,0]]))