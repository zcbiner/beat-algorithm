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
        if head is None:
            return None
        prev = None
        curr = head
        while curr is not None:
            # 先记录下一个节点，否则等下curr.next指向前一个结点会丢失
            next_node = curr.next
            # 指向上一个结点完成翻转
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

# @lc code=end