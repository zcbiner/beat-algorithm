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

    def isPalindrome(self, head):
        # 快慢指针找中点
        p_slow = head
        p_fast = head
        # p_rev指向前半部分反转的链表
        p_rev = None
        while p_fast and p_fast.next:
            p_temp = p_slow
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            p_temp.next = p_rev
            p_rev = p_temp
        if p_fast:
            p_slow = p_slow.next
        while p_rev and p_slow:
            if p_rev.val != p_slow.val:
                return False
            p_rev = p_rev.next
            p_slow = p_slow.next
        return True
# @lc code=end
