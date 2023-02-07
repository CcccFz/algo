#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(cur):
            if not cur:
                return 0
            left_height, right_height = height(cur.left), height(cur.right)
            nonlocal ret
            if not ret or abs(left_height-right_height) > 1:
                ret = False
                return
            return max(left_height, right_height) + 1

        ret = True
        height(root)
        return ret
# @lc code=end

