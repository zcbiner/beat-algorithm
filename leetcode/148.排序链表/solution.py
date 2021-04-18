#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 合并两个链表
    def _mergeList(self, l1, l2):
        result = ListNode(0)
        p_curr = result
        while l1 and l2:
            if l1.val > l2.val:
                p_curr.next = l2
                l2 = l2.next
            else:
                p_curr.next = l1
                l1 = l1.next
            p_curr = p_curr.next
        # l1或l2比对方多的部分直接拼接上
        if l1:
            p_curr.next = l1
        elif l2:
            p_curr.next = l2
        return result.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 将两个链表断开
        pre.next = None
        l1 = self.sortList(slow)
        l2 = self.sortList(head)
        return self._mergeList(l1, l2)

# @lc code=end

