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
    # 从中点拆分成两个链表
    def _splitList(self, head):
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        middle = p_slow.next
        return head,middle

    def isPalindrome(self, head):
        if not head:
            return False
        
        a, b = self._splitList(head)
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
# @lc code=end

