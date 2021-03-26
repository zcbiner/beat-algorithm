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
        if head is None:
            return None
        p_fast = head
        guard_node = ListNode(0, head)
        p_pre = guard_node
        count = 1
        while p_fast is not None:
            if count >= n:
                p_pre = p_pre.next
            p_fast = p_fast.next
            count = count + 1
        # 进行删除
        p_pre.next = p_pre.next.next
        return guard_node.next
# @lc code=end