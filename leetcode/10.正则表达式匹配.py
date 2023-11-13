#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rmatch(s, p, si, pi):
            if pi == len(p):
                if si == len(s):
                    return True
                return False
            if pi+1 < len(p) and p[pi+1] == '*':
                if rmatch(s, p, si, pi+2):
                    return True
                for i in range(si, len(s)):
                    if p[pi] == '.' or p[pi] == s[i]:
                        if rmatch(s, p, i+1, pi+2):
                            return True
                    else:
                        break
            else:
                if si < len(s) and (p[pi] == '.' or p[pi] == s[si]):
                    if rmatch(s, p, si+1, pi+1):
                        return True
            return False
        
        
        return rmatch(s, p, 0, 0)
# @lc code=end
s = Solution()
print(s.isMatch('aa', 'a'))
print(s.isMatch('aa', 'a*'))
print(s.isMatch('ab', '.*'))
print(s.isMatch('aab', 'c*a*b'))
print(s.isMatch('mississippi', 'mis*is*p*.'))
