#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        node_queue = [root]
        res = []
        while node_queue:
            level_list = []
            # 这里一定要根据当前队列的size来遍历，这个size表示属于当层的结点数。
            for i in range(len(node_queue)):
                node = node_queue.pop(0)
                level_list.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            res.append(level_list)
        return res
# @lc code=end