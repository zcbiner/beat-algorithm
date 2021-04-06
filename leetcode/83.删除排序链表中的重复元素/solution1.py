#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p_curr = head
        while p_curr:
            while p_curr.next and p_curr.next.val == p_curr.val:
                p_curr.next = p_curr.next.next
            p_curr = p_curr.next
        return head
# @lc code=end
