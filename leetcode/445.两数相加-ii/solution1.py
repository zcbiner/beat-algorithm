#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        p1 = l1
        while p1:
            num1 = num1 * 10 + p1.val
            p1 = p1.next
        num2 = 0
        p2 = l2
        while p2:
            num2 = num2 * 10 + p2.val
            p2 = p2.next
        
        str_sum = str(num1 + num2)
        p_result = ListNode(0)
        p_curr = p_result
        for item in str_sum:
            p_curr.next = ListNode(int(item))
            p_curr = p_curr.next
        return p_result.next
# @lc code=end

