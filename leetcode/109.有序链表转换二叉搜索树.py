#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_root(low, high):
            if low > high:
                return
            mid = low+((high-low)>>1)
            root = TreeNode(vals[mid])
            root.left = get_root(low, mid-1)
            root.right = get_root(mid+1, high)
            return root

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        return get_root(0, len(vals)-1)
# @lc code=end

