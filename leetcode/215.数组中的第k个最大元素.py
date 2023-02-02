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
        def partition(nums, low, high):
            idx = random.randint(low, high)
            nums[idx], nums[high] = nums[high], nums[idx]
            i = low
            for j in range(low, high):
                if nums[j] > nums[high]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        
        def quick_sort(nums, low, high):
            if low > high:
                return -1
            mid = partition(nums, low, high)
            if mid + 1 < k:
                return quick_sort(nums, mid + 1, high)
            elif mid + 1 > k:
                return quick_sort(nums, low, mid - 1)
            else:
                return nums[mid]
        
        return quick_sort(nums, 0, len(nums)-1)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     return nums[-k]
# @lc code=end
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))