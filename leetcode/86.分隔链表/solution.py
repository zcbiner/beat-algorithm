#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0, head)
        p_anchor = None
        p_curr = dummy
        while p_curr and p_curr.next:
            if p_curr.next.val >= x and not p_anchor:
                p_anchor = p_curr
            elif p_curr.next.val < x and p_anchor:
                a = p_anchor.next
                b = p_curr.next
                p_curr.next = p_curr.next.next
                p_anchor.next = b
                b.next = a
                p_anchor = b
                continue
            p_curr = p_curr.next
        return dummy.next
# @lc code=end

