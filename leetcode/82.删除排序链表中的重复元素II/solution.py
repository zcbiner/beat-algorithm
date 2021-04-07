#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 哨兵结点
        dummy = ListNode(0, head)
        p_mark_head = ListNode(0)
        p_mark_curr = p_mark_head
        p_curr = head
        p_curr_pre = dummy
        # 先扫描，将标记链表对应要删除的结点值置为1
        while p_curr:
            mark_node = None
            if p_curr.val == p_curr_pre.val:
                mark_node = ListNode(1)
                # 由于重复的元素都要删除，所以前一个元素也要置为1
                p_mark_curr.val = 1
            else:
                mark_node = ListNode(0)
            p_mark_curr.next = mark_node
            p_mark_curr = mark_node
            p_curr = p_curr.next
            p_curr_pre = p_curr_pre.next

        p_mark_curr = p_mark_head.next
        p_curr = head.next
        p_curr_pre = dummy
        # 标记链表和原链表长度一致，同时遍历两个链表。
        # 标记链表中值为1的结点表示原链表对应结点要删除。
        while p_curr:
            next_node = p_curr.next
            if p_mark_curr.val == 1:
                p_curr_pre.next = next_node
                p_curr.next = None
            else:
                p_curr_pre = p_curr_pre.next
            p_curr = next_node
            p_mark_curr = p_mark_curr.next
        
        return dummy.next
# @lc code=end

