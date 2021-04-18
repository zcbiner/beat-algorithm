### 题目
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例1：
```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

示例2：
```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

示例 3：
```
输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
```

示例 4：
```
输入：head = [1], k = 1
输出：[1]
```

提示：
- 列表中节点的数量在范围 sz 内
- 1 <= sz <= 5000
- 0 <= Node.val <= 1000
- 1 <= k <= sz

### 解题
每k个一组进行翻转，每一组有k个，也就是说[0,k],[k+1, 2k]等每个组组内结点进行翻转。

#### 解法一
翻转单个组很简单，把一组看做一个独立的链表，就可以按照题目:[206.反转链表](../206.反转链表/readme.md)的解法完成。

[代码实现](solution.py)：
```py
class Solution:

    # 翻转一个链表
    def _reverse(self, head):
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        p_pre = dummy
        p_curr = head
        # index用来记录遍历结点数，满k则翻转一次链表，然后重置。
        index = 1
        while p_curr:
            if index == k:
                # p_last指向当前组的下一个结点。
                p_last = p_curr.next
                p_curr.next = None
                p_reversed = self._reverse(p_pre.next)
                p_temp = p_pre.next
                p_temp.next = p_last
                p_pre.next = p_reversed
                p_pre = p_temp
                p_curr = p_last
                index = 1
            else:
                index += 1
                p_curr = p_curr.next
        return dummy.next
```
自己想出来的解法，在``index==k``这种情况时有比较多的指针操作，很容易出错，需要画图明确各个指针的作用。

#### 解法二
LeetCode的Top voted solution是这样做的：
```py
class Solution:

    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
    
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next
```
拿[1,2,3,4,5]举例：
- 初始化时，l、r都指向头结点1
- while循环后r指向3。由于k为2，[1,2]是为一组的，所以r是定位到了下一组的第一个结点
- while循环后，count等于k说明满一组，需要对着一组中的链表进行翻转
- ``if count == k``中对一组中的链表进行了翻转，翻转后的链表为：[2,1,3,4,5]并最后更新l、r的值为1、3
- 进行下一次while循环

