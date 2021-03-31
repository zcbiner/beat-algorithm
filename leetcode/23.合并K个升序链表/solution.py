#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        dummy = ListNode(0)
        p1 = lists[0]
        # 进行两两合并。
        for i in range(1, len(lists)):
            p1 = self.merge_two_lists(p1, lists[i])
            dummy.next = p1

        return dummy.next

    # 合并两个升序链表，查看21题的解法。
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

# @lc code=end

