#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
from typing import List
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                ans[j] += ans[j-1]
            if i == rowIndex:
                return ans
# @lc code=end
s = Solution()
print(s.getRow(3))  # [1,3,3,1]
print(s.getRow(0))  # [1]
print(s.getRow(1))  # [1,1]