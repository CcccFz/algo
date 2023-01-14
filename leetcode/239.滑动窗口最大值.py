#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        if size <= 1 or k == 0:
            return nums
        ret, queue = [], []
        for i in range(size):
            if queue and queue[0] == i - k:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret
# @lc code=end
s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))