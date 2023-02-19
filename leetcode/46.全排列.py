#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(first):
            if first == len(nums):
                ans.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                _permute(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        ans = []
        _permute(0)
        return ans
# @lc code=end
s = Solution()
print(s.permute([1,2,3]))
print(s.permute([0,1]))
print(s.permute([1]))
