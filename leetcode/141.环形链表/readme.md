> 题目：[环形链表](https://leetcode-cn.com/problems/linked-list-cycle/description/)。

### 解题
经典题目，判断链表是否有环，用**快慢指针**解决。
- p1，p2分别为快慢指针。p1每次向前遍历一个结点，p2每次向前遍历两个结点。
- 当p1，p2相遇，则链表有环。

[代码实现](solution.py)：
```py
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False
```