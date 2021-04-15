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
        # 两个链表的值分别入栈
        stack1 = []
        p1 = l1
        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        
        stack2 = []
        p2 = l2
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        
        # new_head链表存放相加得到的值，此时得到的结果链表低位存放的是和的低位
        new_head = ListNode(0)
        p_new_head = new_head
        num = 0
        while stack1 or stack2 or num > 0:
            if stack1:
                num += stack1.pop()
            if stack2:
                num += stack2.pop()
            next_node = None
            if num >= 10:
                next_node = ListNode(num%10)
                # 用于进位
                num = 1
            else:
                next_node = ListNode(num)
                num = 0
            p_new_head.next = next_node
            p_new_head = next_node
        # 逆序new_head得到正确的值
        new_head = new_head.next
        result = None
        while new_head:
            next_node = new_head.next
            new_head.next = result
            result = new_head
            new_head = next_node
        return result
        
# @lc code=end

