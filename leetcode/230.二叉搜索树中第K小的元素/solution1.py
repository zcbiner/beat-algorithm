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
        self.k = k
        self._traversal(root)
        return self.ans

    def _traversal(self, root: TreeNode):
        if not root:
            return
        
        self._traversal(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return
        self._traversal(root.right)
# @lc code=end

