#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1    
        cur = 0
        while cur <= right:
            if nums[cur] == 0 and cur >= left:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
            elif nums[cur] == 2:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            else:
                cur += 1

# @lc code=end
s = Solution()
items = [2,0,2,1,1,0]
s.sortColors(items)
print(items)
items = [2,0,1]
s.sortColors(items)
print(items)