> 题目：[移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements/description/)。

### 解题
考查的是对链表结点的删除操作，非常简单。

[代码实现](solution.py)：
```py
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(0, head)
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
```

检查p.next的值是否为val，如果是则执行：``p.next = p.next.next``，将p.next结点删除。注意这种情况删除后，不需要执行``p = p.next``，因为可能删除完的下一个结点值也为val。
