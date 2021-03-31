#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        result = None
        p_result = None
        while p1 or p2:
            p_temp = None
            if p1 is None:
                p_temp = p2
                p2 = p2.next
            elif p2 is None:
                p_temp = p1
                p1 = p1.next
            else:
                if p1.val > p2.val:
                    p_temp = p2
                    p2 = p2.next
                else:
                    p_temp = p1
                    p1 = p1.next
            if result is None:
                result = p_temp
                p_result = result
            else:
                p_result.next = p_temp
                p_result = p_result.next
        return result
# @lc code=end
