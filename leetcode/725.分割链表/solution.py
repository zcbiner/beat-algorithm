#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        p_curr = root
        node_size = 0
        while p_curr:
            node_size += 1
            p_curr = p_curr.next
        count = node_size // k
        remainder = node_size % k
        result = []
        p_curr = root
        # 分割成k部分
        for i in range(k):
            split_size = count
            if remainder > 0:
                split_size += 1
                remainder -= 1
            new_head = p_curr
            # 找到分割的前一个结点
            while split_size > 1 and p_curr:
                split_size -= 1
                p_curr = p_curr.next
            if p_curr:
                p_temp = p_curr
                p_curr = p_curr.next
                p_temp.next = None
            result.append(new_head)
        return result
        
# @lc code=end

