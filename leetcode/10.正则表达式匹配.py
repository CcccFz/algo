#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rmatch(s, p, s_i, p_i):
            if self.matched:
                return
            if p_i == len(p):
                if s_i == len(s):
                    self.matched = True
                return
            if p[p_i] == '*':
                for i in range(s_i, len(s)+1):
                    rmatch(s, p, i, p_i+1)
            elif p[p_i] == '.':
                rmatch(s, p, s_i+1, p_i+1)
            elif s_i < len(s) and s[s_i] == p[p_i]:
                rmatch(s, p, s_i+1, p_i+1)

        self.matched = False
        rmatch(s, p, 0, 0)
        return self.matched
# @lc code=end
s = Solution()
print(s.isMatch('aa', 'a'))
print(s.isMatch('aa', 'a*'))
print(s.isMatch('ab', '.*'))
