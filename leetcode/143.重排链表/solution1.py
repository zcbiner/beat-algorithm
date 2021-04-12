#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 拆分链表，将链表从中间断开分为两个链表
    def _splitList(self, head):
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        
        middle = p_slow.next
        p_slow.next = None
        return head, middle

    # 翻转一个链表
    def _reverseList(self, head):
        new_head = None
        p = head
        while p:
            next_node = p.next
            p.next = new_head
            new_head = p
            p = next_node
        return new_head

    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        a,b = self._splitList(head)
        b = self._reverseList(b)
        
        # 将a，b合并
        while a and b:
            a_next = a.next
            b_next = b.next
            a.next = b
            b.next = a_next
            b = b_next
            a = a_next

# @lc code=end