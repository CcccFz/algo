#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
def is_valid(c):
    return ('a' <= c and c <= 'z') or ('0' <= c and c <= '9')

class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     i, j = 0, len(s)-1
    #     while i < j:
    #         if not is_valid(s[i]):
    #             i += 1
    #             continue
    #         if not is_valid(s[j]):
    #             j -= 1
    #             continue
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True

    def isPalindrome(self, s: str) -> bool:
        

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     items = [c for c in s if c.isalnum()]
    #     s = ''.join(items)
    #     return s == s[::-1]

# @lc code=end
solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
print(solution.isPalindrome(' '))