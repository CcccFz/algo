#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + ((high-low)>>1)
            if mid * mid > x:
                high = mid - 1
            else:
                if (mid+1) * (mid+1) > x:
                    return mid
                low = mid + 1
        return -1
# @lc code=end
s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
