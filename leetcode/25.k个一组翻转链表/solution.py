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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        p_fast = head
        for i in range(k - 1):
            p_fast = p_fast.next
        
        p_curr = head
        while p_fast:
            
        
        p_curr = head
        while node_size > k:
            


# @lc code=end

