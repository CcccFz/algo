#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def in_order(cur):
            if cur:
                if not in_order(cur.left):
                    return False
                nonlocal last
                if cur.val <= last:
                    return False
                last = cur.val
                if not in_order(cur.right):
                    return False
            return True

        last = -math.inf
        return in_order(root)
# @lc code=end

