#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def get_root(low, high):
            if low > high:
                return
            mid = low+((high-low)>>1)
            root = TreeNode(nums[mid])
            root.left = get_root(low, mid-1)
            root.right = get_root(mid+1, high)
            return root

        return get_root(0, len(nums)-1)
# @lc code=end

