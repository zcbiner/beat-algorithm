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
        stack = []
        node = root
        pre_val = None
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            if len(stack) == 0:
                return True
            
            curr_node = stack.pop()
            if pre_val is not None and pre_val >= curr_node.val:
                return False
            pre_val = curr_node.val
            node = curr_node.right
# @lc code=end