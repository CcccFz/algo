#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right-left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     return self.search_recursion(nums, 0, len(nums)-1, target)

    # def search_recursion(self, nums: List[int], left: int, right: int, target: int) -> int:
    #     if left > right:
    #         return -1
    #     mid = left + ((right-left) >> 1)
    #     if nums[mid] < target:
    #         return self.search_recursion(nums, mid+1, right, target)
    #     elif nums[mid] > target:
    #         return self.search_recursion(nums, left, mid-1, target)
    #     return mid

    

# @lc code=end
s = Solution()
print(s.search([-1,0,3,5,9,12], 9))
print(s.search([-1,0,3,5,9,12], 2))