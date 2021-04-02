#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(0, head)
        # 左侧开始反转的结点
        p_left = head
        # 开始p_left的前一个结点
        p_left_pre = dummy
        # 右侧反转结束的结点
        p_right = None
        # p_right的后一个结点
        p_right_after = None
        # 当前遍历指向的结点
        p_curr = head
        # 当前遍历结点的前一个结点
        p_curr_pre = dummy
        # 遍历到第几个结点
        curr_index = 1
        while p_curr:
            if curr_index == (left - 1):
                p_left_pre = p_curr
                p_left = p_curr.next
            if right == curr_index:
                p_right = p_curr
                p_right_after = p_curr.next
            
            p_curr_after = p_curr.next
            # 进行链表翻转
            if curr_index > left and curr_index <= right:
                p_curr.next = p_curr_pre

            p_curr_pre = p_curr
            p_curr = p_curr_after
            curr_index = curr_index + 1
        # left前一结点指向right结点
        p_left_pre.next = p_right
        # left结点指向right后一个结点
        p_left.next = p_right_after
        return dummy.next
# @lc code=end

