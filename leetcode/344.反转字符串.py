#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low, high = 0, len(s)-1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
# @lc code=end
s = Solution()
ret = ["h","e","l","l","o"]
s.reverseString(ret)
print(ret)
ret = ["H","a","n","n","a","h"]
s.reverseString(ret)
print(ret)
