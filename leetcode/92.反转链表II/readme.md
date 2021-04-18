### 题目
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 
示例 1：
```
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
```

示例 2：
```
输入：head = [5], left = 1, right = 1
输出：[5]
```

提示：
- 链表中节点数目为 n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

进阶： 你可以使用一趟扫描完成反转吗？

### 解题
如何翻转链表结点呢？就是把当前结点的指针指向前一个结点。具体看[206.反转链表](../206.反转链表/readme.md)的解题。

在这道题中，我只要翻转left到right的结点就行了。翻转完后处理下left和right这两个结点的指向，题目就完成了。

代码实现:[solution.py](solution.py):
```py
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(0, head)
        # 左侧开始反转的结点
        p_left = head
        # 开始p_left的前一个结点
        p_left_pre = dummy
        # 右侧反转结束的结点
        p_right = None
        # p_right的后一个结点
        p_right_after = None
        # 当前遍历指向的结点
        p_curr = head
        # 当前遍历结点的前一个结点
        p_curr_pre = dummy
        # 遍历到第几个结点
        curr_index = 1
        while p_curr:
            if curr_index == (left - 1):
                p_left_pre = p_curr
                p_left = p_curr.next
            if right == curr_index:
                p_right = p_curr
                p_right_after = p_curr.next
            
            p_curr_after = p_curr.next
            # 进行链表翻转
            if curr_index > left and curr_index <= right:
                p_curr.next = p_curr_pre

            p_curr_pre = p_curr
            p_curr = p_curr_after
            curr_index = curr_index + 1
        # left前一结点指向right结点
        p_left_pre.next = p_right
        # left结点指向right后一个结点
        p_left.next = p_right_after
        return dummy.next
```