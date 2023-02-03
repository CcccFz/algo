#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = []
        for i, c in enumerate(s):
            if stack and c == ')' and s[stack[-1]] == '(':
                stack.pop()
                if stack:
                    longest = max(longest, i-stack[-1])
                else:
                    longest = i + 1
            else:
                stack.append(i)
        return longest
# @lc code=end
s = Solution()
print(s.longestValidParentheses('(()'))
print(s.longestValidParentheses(')()())'))
print(s.longestValidParentheses(''))
