#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def _splitList(self, head):
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next
        if p_fast:
            p_slow = p_slow.next
        return head, p_slow

    def _reverseList(self, head):
        new_head = None
        while head:
            next_node = head
            head.next = new_head
            new_head = head
            head = next_node
        return new_head
        

    def isPalindrome(self, head):
        a, b = self._splitList(head)
        print(a.val)
        print(b.val)
        b = self._reverseList(b)
        print(b.val)
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
# @lc code=end

