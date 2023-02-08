#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def pre_order(cur):
            if cur:
                nodes.append(cur)
                pre_order(cur.left)
                pre_order(cur.right)

        nodes = []
        pre_order(root)

        for i in range(1, len(nodes)):
            cur, next = nodes[i-1], nodes[i]
            cur.left = None
            cur.right = next

    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                prev, next = cur.left, cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.left = None
                cur.right = next
            cur = cur.right
                
# @lc code=end

