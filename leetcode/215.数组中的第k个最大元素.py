#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

from typing import List
# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k-1
        self.quick_sort(nums, 0, len(nums)-1)
        return nums[self.k]

    def quick_sort(self, nums: List[int], start, end: int) -> int:
        if start < end:
            mid = self.partition(nums, start, end)
            if mid == self.k:
                return
            elif mid > self.k:
                return self.quick_sort(nums, start, mid-1)
            elif mid < self.k:
                return self.quick_sort(nums, mid+1, end)
            
    def partition(self, nums: List[int], start, end: int) -> int:
        idx = random.randint(start, end)   
        nums[end], nums[idx] = nums[idx], nums[end]

        i = start
        for j in range(start, end):
            if nums[j] > nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     return nums[-k]
# @lc code=end
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))