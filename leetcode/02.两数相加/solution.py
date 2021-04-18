#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        result = ListNode(0, None)
        p_result = result
        while p1 or p2:
            # val_sum为两个结点相加的和，初始化为p_result.val是因为它可能有进位的值。
            val_sum = p_result.val
            if p1:
               val_sum += p1.val
               p1 = p1.next
            if p2:
               val_sum += p2.val
               p2 = p2.next
            if val_sum >= 10:
                # next结点用于存放进位的值
                p_result.next = ListNode(1, None)
                p_result.val = val_sum % 10
            else:
                p_result.val = val_sum
                # 如果p1，p2为空了，和就没有下一个结点了
                if p1 or p2:
                    p_result.next = ListNode(0, None)
            p_result = p_result.next

        return result

# @lc code=end

