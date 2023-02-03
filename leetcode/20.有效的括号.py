#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','[':']','{':'}'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack or c != dic[stack.pop()]:
                    return False
        return not stack
# @lc code=end

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("[(())]"))
print(s.isValid(""))

