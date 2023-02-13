#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#
from typing import List

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eated, n, ans = {}, len(candyType)/2, 0
        for _type in candyType:
            if _type in eated:
                continue
            eated[_type] = True
            ans += 1
            if ans == n:
                break
        return ans
# @lc code=end
s = Solution()
print(s.distributeCandies([1,1,2,2,3,3])) # 3
print(s.distributeCandies([1,1,2,3]))     # 2
print(s.distributeCandies([6,6,6,6]))     # 1
