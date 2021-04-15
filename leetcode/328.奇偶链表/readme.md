> 题目：[奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/description/)。

### 解题
题目要求是把一个链表中的所有奇数结点都放到链表的前半部分，把所有的偶数链表放到后半部分。

题目的额外要求：
1. 时间复杂度为O(n)，空间复杂度为O(1)
2. 应当保持奇数节点和偶数节点的相对顺序
3. 请尝试使用原地算法完成

使用两个指针，p_odd指向所有的奇数结点，p_even指向所有的偶数结点。
head对原链表进行遍历，遇到奇数结点则使用p_odd指向它，更新p_odd。反之遇到偶数结点使用p_even指向它，更新p_even。

使用哨兵结点简化操作，不用额外判断原链表是否为null等情形。

[代码实现](solution.py)：
```py
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p_odd = ListNode(0)
        p_odd_head = p_odd
        p_even = ListNode(0)
        p_even_head = p_even
        while head:
            p_odd.next = head
            p_odd = p_odd.next
            p_even.next = head.next
            p_even = p_even.next
            if head.next:
                head = head.next.next
            else:
                break
        p_odd.next = p_even_head.next
        return p_odd_head.next
```
