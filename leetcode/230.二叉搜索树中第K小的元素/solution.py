#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val_list = []
        self._traversal(root, val_list)
        return val_list[k - 1]

    def _traversal(self, root: TreeNode, val_list: List[int]):
        if not root:
            return -1
        
        self._traversal(root.left, val_list)
        val_list.append(root.val)
        self._traversal(root.right, val_list)

# @lc code=end

