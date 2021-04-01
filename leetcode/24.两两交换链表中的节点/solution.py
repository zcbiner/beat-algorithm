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
        p1 = head
        p2 = head.next
        while p1 is not None and p2 is not None:
            # 将p1，p2节点互换
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            # 更新pre，p1，p2指向节点，进行下一轮的互换
            pre = p1
            p1 = p1.next
            if p1 is None:
                break
            p2 = p1.next
            if p2 is None:
                break
        return dummy.next
            

# @lc code=end

