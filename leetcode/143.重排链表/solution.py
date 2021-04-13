#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and head.next:
            return
        # 将链表结点存放到数组中
        array = []
        p = head
        while p:
            array.append(p)
            p = p.next
        
        array_size = len(array)
        # i, j分别指向左右的两个结点
        i = 0
        j = array_size - 1
        while i < j:
            array[i].next = array[j]
            i += 1
            if i == j:
                break

            array[j].next = array[i]
            j -= 1
            array[j].next = None
# @lc code=end