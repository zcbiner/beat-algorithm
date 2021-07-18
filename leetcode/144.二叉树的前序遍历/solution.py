#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._traversal(root, res)
        return res

    def _traversal(self, root: TreeNode, res: List[int]):
        if not root:
            return
        res.append(root.val)
        self._traversal(root.left, res)
        self._traversal(root.right, res)
# @lc code=end

