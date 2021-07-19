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
        temp_root = root
        result_list = []
        stack = []
        while True:
            while temp_root:
                stack.append(temp_root)
                temp_root = temp_root.left
            
            if len(stack) == 0:
                return result_list
            
            node = stack.pop()
            result_list.append(node.val)
            temp_root = node.right

# @lc code=end

