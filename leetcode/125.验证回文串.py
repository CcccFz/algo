#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_valid(c):
    return ('a' <= c and c <= 'z') or ('0' <= c and c <= '9')

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if 'a' <= c <= 'z' or '0' <= c <= '9']
        low, high = 0, len(s)-1
        while low <= high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     items = [c for c in s if c.isalnum()]
    #     s = ''.join(items)
    #     return s == s[::-1]

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     dummy = Node(None)
    #     head = dummy
    #     for c in s:
    #         if not c.isalnum():
    #             continue
    #         dummy.next = Node(c)
    #         dummy = dummy.next
    #     dummy.next = None
    #     dummy = head
    #     head = head.next

    #     slow, fast = head, head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
        
    #     prev = None
    #     while slow:
    #         cur = slow
    #         slow = slow.next
    #         cur.next = prev
    #         prev = cur
        
    #     while head and prev:
    #         if head.val != prev.val:
    #             return False
    #         head = head.next
    #         prev = prev.next

    #     return True


        
# @lc code=end
solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
print(solution.isPalindrome(' '))