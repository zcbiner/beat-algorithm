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
        
        # 取中点
        mid = len(lists) // 2
        # 拆分链表
        l1,l2 = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # 两两合并
        return self.merge_two_lists(l1, l2)

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

