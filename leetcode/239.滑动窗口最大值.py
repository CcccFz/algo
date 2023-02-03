#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        ret = [nums[queue[0]]]
        for i in range(k, len(nums)):
            if i-k == queue[0]:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            ret.append(nums[queue[0]])
        return ret
# @lc code=end
s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))