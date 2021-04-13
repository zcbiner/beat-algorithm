> 题目：[对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/description/)。

### 解题
可以先看看如何对数组进行插入排序的：[例子](../../sorting-algorithm/src/insert_sort.py)。

单链表的问题在于，无法像数组一样，从已排序部分的结尾进行遍历处理。

这样的话，就用一个哨兵结点指向已排序的部分，然后从未排序的部分取结点从哨兵结点开始比较。并将该结点插入到对应的位置。
[代码实现](solution.py):
```py
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
```

代码中，head始终为未排序部分的头结点。dummy为已排序链表的哨兵结点。每次都从head链表中取头结点p_curr，然后从dummy开始遍历，定位到比p_curr大的前一个结点p_insert。然后把p_curr插入到dummy结点中。
最后dummy链表就是经过插入排序处理的有序链表了。时间复杂度为O(n^2)。