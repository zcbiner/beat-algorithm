### 题目
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

示例 2：
```
输入：l1 = [0], l2 = [0]
输出：[0]
```

示例 3：
```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```
 

提示：
- 每个链表中的节点数在范围 [1, 100] 内
- 0 <= Node.val <= 9
- 题目数据保证列表表示的数字不含前导零

### 解题
看下题目，感觉很简单啊。分别用两个指针遍历两个链表，将相同位置的数字加起来就行了。期间要注意：
- 需要判断是否要进位
- 如果两个链表长度不一样，需要处理。

代码实现如下：

```py
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        result = ListNode(0, None)
        p_result = result
        while p1 is not None or p2 is not None:
            # val_sum为两个结点相加的和，初始化为p_result.val是因为它可能有进位的值。
            val_sum = p_result.val
            if p1 is not None:
               val_sum += p1.val
               p1 = p1.next
            if p2 is not None:
               val_sum += p2.val
               p2 = p2.next
            if val_sum >= 10:
                # next结点用于存放进位的值
                p_result.next = ListNode(1, None)
                p_result.val = val_sum % 10
            else:
                p_result.val = val_sum
                # 如果p1，p2为空了，和就没有下一个结点了
                if p1 is not None or p2 is not None:
                    p_result.next = ListNode(0, None)
            p_result = p_result.next

        return result
```