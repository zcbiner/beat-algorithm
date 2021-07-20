#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        val_list = []
        self._in_order(root, val_list)
        size = len(val_list)
        for i in range(1, size):
            if val_list[i - 1] >= val_list[i]:
                return False
        return True

    def _in_order(self, node: TreeNode, val_list: List[int]):
        if not node:
            return
        self._in_order(node.left, val_list)
        val_list.append(node.val)
        self._in_order(node.right, val_list)
# @lc code=end