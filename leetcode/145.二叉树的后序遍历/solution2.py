#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res
# @lc code=end

