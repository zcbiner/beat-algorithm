#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0 or not head.next:
            return head
        p = head
        list_size = 1
        while p.next:
            p = p.next
            list_size = list_size + 1
        
        if k == list_size:
            return head
        # 头结点和尾结点相连，形成环
        p.next = head
        # k大于结点数，大于的部分是绕了一圈
        while k > list_size:
            k = k % list_size
        pre = head
        for i in range(list_size - k - 1):
            pre = pre.next
        
        head = pre.next
        # 切断环
        pre.next = None
        return head

# @lc code=end

