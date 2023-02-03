#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        cur, next = 1, 2
        for _ in range(1, n):
            cur, next = next, cur+next
        return cur
# @lc code=end
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
