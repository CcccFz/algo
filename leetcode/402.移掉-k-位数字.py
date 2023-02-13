#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remain = len(num) - k
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        return ''.join(stack[:remain]).lstrip('0') or '0'
# @lc code=end
s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("10200", 1))
print(s.removeKdigits("10", 2))
