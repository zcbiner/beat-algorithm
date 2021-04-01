#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            # p1，p2指向两个要交换的节点点
            p1 = pre.next
            p2 = pre.next.next
            # 进行交换
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            # 更新pre，进行下一轮替换
            pre = p1
        return dummy.next
# @lc code=end

