#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from math import inf

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        def bfs(root):
            queue = deque([root])
            while queue:
                max_val = -inf
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                    if node.val > max_val: max_val = node.val
                ans.append(max_val)

        def dfs(root, level=0):
            if not root:
                return
                
            if level == len(ans):
                ans.append(root.val)
            elif root.val > ans[level]:
                ans[level] = root.val

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root)
        # bfs(root)
        return ans
# @lc code=end

