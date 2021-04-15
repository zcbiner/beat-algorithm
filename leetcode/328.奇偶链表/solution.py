#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p_odd = ListNode(0)
        p_odd_head = p_odd
        p_even = ListNode(0)
        p_even_head = p_even
        while head:
            p_odd.next = head
            p_odd = p_odd.next
            p_even.next = head.next
            p_even = p_even.next
            if head.next:
                head = head.next.next
            else:
                break
        p_odd.next = p_even_head.next
        return p_odd_head.next

# @lc code=end

