#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, l1, l2 = ListNode(-1), list1, list2
        l = head
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = l1 if l1 else l2
        return head.next
# @lc code=end

