#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 翻转一个链表
    def _reverse(self, head):
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        p_pre = dummy
        p_curr = head
        # index用来记录遍历结点数，满k则翻转一次链表，然后重置。
        index = 1
        while p_curr:
            if index == k:
                p_last = p_curr.next
                p_curr.next = None
                p_reversed = self._reverse(p_pre.next)
                p_temp = p_pre.next
                p_temp.next = p_last
                p_pre.next = p_reversed
                p_pre = p_temp
                p_curr = p_last
                index = 1
            else:
                index += 1
                p_curr = p_curr.next
        return dummy.next

# @lc code=end

