#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result_list = []
        self._traversal(root, result_list)
        return result_list

    def _traversal(self, root: TreeNode, result_list: List[int]):
        if not root:
            return
        
        self._traversal(root.left, result_list)
        result_list.append(root.val)
        self._traversal(root.right, result_list)

# @lc code=end

