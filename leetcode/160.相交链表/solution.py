#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        point_a = headA
        point_b = headB

        while point_a is not point_b:
            point_a = headB if point_a is None else point_a.next
            point_b = headA if point_b is None else point_b.next
        
        return point_a
        
# @lc code=end