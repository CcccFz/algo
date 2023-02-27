#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([1]*(i+1))
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
# @lc code=end
s = Solution()
print(s.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(s.generate(1)) # [[1]]
