#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        p_fast = head
        p_slow = head
        pre = head
        for i in range(1, n):
            if p_fast.next is None:
                return None
            p_fast = p_fast.next
        while p_fast.next is not None:
            if p_slow is not head:
                pre = pre.next
            p_fast = p_fast.next
            p_slow = p_slow.next

        # p_slow为头结点，说明要删除的是头结点
        if p_slow is head:
            return head.next
        # 进行删除
        pre.next = pre.next.next
        return head
# @lc code=end

