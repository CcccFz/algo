#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high, size = 0, len(nums)-1, len(nums)
        while low <= high:
            mid = low+((high-low)>>1)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                first, last = mid, mid
                while first != 0 and nums[first-1] == target:
                    first -= 1
                while last != size-1 and nums[last+1] == target:
                    last += 1
                return [first, last]
        return [-1, -1]
# @lc code=end
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([], 0))