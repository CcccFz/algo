#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = -1
        while left <= right:
            mid = left + ((right-left)>>1)
            if mid * mid > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans
# @lc code=end
s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
