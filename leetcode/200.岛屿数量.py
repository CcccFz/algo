#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start
from collections import deque

class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        def is_in_area(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        ans = 0
        queue = deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    ans += 1
                    queue.append((x, y))
                    while queue:
                        i, j = queue.popleft()
                        if not is_in_area(i,j) or grid[i][j] == '0':
                            continue
                        grid[i][j] = '0'
                        queue.append((i,j-1))
                        queue.append((i,j+1))
                        queue.append((i-1,j))
                        queue.append((i+1,j))
        return ans

    def numIslands(self, grid: List[List[str]]) -> int:
        def in_area(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i, j):
            if not in_area(i,j) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i+1, j)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans
# @lc code=end
s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))   # 1

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3
