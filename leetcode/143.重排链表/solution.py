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
import math as m
from ..dataStruct import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 求出单链表节点数
        p = head
        count = 0
        while p:
            p = p.next
            count = count + 1

        print(count)
        # 计算
        nodeMiddle = m.ceil((count - 1) / 2)
        p = head
        index = 0
        middle = (count - 1) / 2
        stack = []
        while p: 
            if index >= middle:
                stack.append(p)
            p = p.next
        
        p = head
        index = 0
        while p:
            if index < middle and index > 0:
                b = stack.pop()
                b.next = p.next
                p.next = b
            p = p.next
# @lc code=end

if __name__ == '__main__':
    head = buildListNode([1,2,3,4])
    Solution().reorderList(head)