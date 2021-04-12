> 题目：[重排链表](https://leetcode-cn.com/problems/reorder-list/description/)。

### 解题
#### 利用数组解题
这里如果是数组的话，就很好操作，因为数组可以直接根据索引来找到元素。

可是这里是单链表，只能单向遍历获取元素。**那我就把链表先转成数组，操作完再把数组转换为单链表。**

操作方法：
1. 链表转换为数组
2. 在数组中完成结点的重排

[代码实现](solution.py)：
```py
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and head.next:
            return
        # 将链表转换为数组
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
```

#### 反转链表解题
利用数组解题，空间复杂度O(n)，在LeetCode上看到了空间复杂度为O(1)的解法。
具体步骤如下：
- 使用快慢指针找到链表的中点，并从中点分割成两个链表a和b
- 将中点后的链表b反转
- 将a，b链表合并成一个。a链表的隔位插入一个b链表的结点

[代码实现](solution1.py)：
```py
class Solution:
    # 拆分链表，将链表从中间断开分为两个链表
    def _splitList(self, head):
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        
        middle = p_slow.next
        p_slow.next = None
        return head, middle

    # 翻转一个链表
    def _reverseList(self, head):
        new_head = None
        p = head
        while p:
            next_node = p.next
            p.next = new_head
            new_head = p
            p = next_node
        return new_head

    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        a,b = self._splitList(head)
        b = self._reverseList(b)
        
        # 将a，b合并
        while a and b:
            a_next = a.next
            b_next = b.next
            a.next = b
            b.next = a_next
            b = b_next
            a = a_next
```
