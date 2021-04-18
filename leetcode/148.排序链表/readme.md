> 题目：[排序链表。](https://leetcode-cn.com/problems/sort-list/description/)

### 解题
#### 分析
注意题目要求：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

这也就意味着不能利用数组或者其它数据结构来辅助，而[147.对链表进行插入排序](../147.对链表进行插入排序/readme.md)题的复杂度为O(n^2)也不满足要求。

数组排序中，满足时间复杂度为O(n log n)的有：
- 快速排序
- 归并排序
- 堆排序

快速排序要求有两个指针分别操作，不适合单链表。单链表只有一个指针域，也不适合堆排序。因此只剩下归并排序可以考虑了。

#### 使用归并排序
归并排序的要点就是使用分治法，将链表不断划分，然后进行合并。
合并两个有序链表的题目之前有做过：[21.合并两个有序链表](../21.合并两个有序链表/readme.md)

[代码实现](solution.py):
```py
class Solution:

    # 合并两个链表
    def _mergeList(self, l1, l2):
        result = ListNode(0)
        p_curr = result
        while l1 and l2:
            if l1.val > l2.val:
                p_curr.next = l2
                l2 = l2.next
            else:
                p_curr.next = l1
                l1 = l1.next
            p_curr = p_curr.next
        # l1或l2比对方多的部分直接拼接上
        if l1:
            p_curr.next = l1
        elif l2:
            p_curr.next = l2
        return result.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 将两个链表断开
        pre.next = None
        l1 = self.sortList(slow)
        l2 = self.sortList(head)
        return self._mergeList(l1, l2)
```