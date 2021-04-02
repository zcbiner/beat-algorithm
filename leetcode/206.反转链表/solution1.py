#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse_list(head, None)

    # new_head指向已翻转结点的头结点
    def reverse_list(self, head: ListNode, new_head: ListNode) -> ListNode:
        if head is None:
            return new_head
        a = head.next
        head.next = new_head
        return self.reverse_list(a, head)

# @lc code=end