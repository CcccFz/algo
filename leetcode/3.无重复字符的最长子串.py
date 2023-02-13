#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, ans = 0, 0
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                low = max(dic[c], low)
            ans = max(ans, i-low+1)
            dic[c] = i+1
        return ans
# @lc code=end
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))