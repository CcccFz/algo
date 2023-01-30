#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max_idx = len(nums)-1
        left, right = 0, max_idx
        while left <= right:
            mid = left + ((right-left)>>1)
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[max_idx]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# @lc code=end
s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1], 0))