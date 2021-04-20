#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        fast = head
        dummy = ListNode(0, head)
        pre = dummy
        count = 1
        while fast and fast.next:
            if count >= n:
                pre = pre.next
            fast = fast.next
            count += 1
        # 进行删除
        pre.next = pre.next.next
        return dummy.next
# @lc code=end