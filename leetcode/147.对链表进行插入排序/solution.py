#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        while head:
            # p_curr代表要进行插入比较的结点。
            p_curr = head
            head = head.next
            # p_insert用于遍历已排序的部分并定位到具体要插入的位置
            p_insert = dummy
            while p_insert and p_insert.next:
                if p_insert.next.val > p_curr.val:
                    break
                p_insert = p_insert.next

            p_curr.next = p_insert.next
            p_insert.next = p_curr
        return dummy.next
# @lc code=end

