#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num], i]
            dic[num] = i
        return []
# @lc code=end
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))
print(solution.twoSum([2,3], 6))
