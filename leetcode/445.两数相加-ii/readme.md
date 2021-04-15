> 题目：[两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/description/)。

### 解题
相比于[02.两数相加](../02.两数相加/readme.md)，区别就在于本题的数字存放顺序不一样。

(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)意味着7243+564=7807。加法都是从低位开始加，加到高位的，所以[02.两数相加](../02.两数相加/readme.md)相对比较简单。

而这里题目还明确要求：
- 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

因此不能翻转链表后复用02题的解法。

#### 利用栈来解题
那能不能用利用栈来解题呢？可以，但是比较麻烦，需要用两个栈分别存放两个链表的值，然后出栈相加得到和。

[代码实现](solution.py)：
```py
class Solution:
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 两个链表的值分别入栈
        stack1 = []
        p1 = l1
        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        
        stack2 = []
        p2 = l2
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        
        # new_head链表存放相加得到的值，此时得到的结果链表低位存放的是和的低位
        new_head = ListNode(0)
        p_new_head = new_head
        num = 0
        while stack1 or stack2 or num > 0:
            if stack1:
                num += stack1.pop()
            if stack2:
                num += stack2.pop()
            next_node = None
            if num >= 10:
                next_node = ListNode(num%10)
                # 用于进位
                num = 1
            else:
                next_node = ListNode(num)
                num = 0
            p_new_head.next = next_node
            p_new_head = next_node
        # 逆序new_head得到正确的值
        new_head = new_head.next
        result = None
        while new_head:
            next_node = new_head.next
            new_head.next = result
            result = new_head
            new_head = next_node
        return result
```

#### 利用数字特性解题
利用栈来解题步骤繁琐，空间复杂度为O(n+m)，显然不是一个很好的解法。
这里可以利用数字特性解题。
- 将两个链表直接分别转为数字，即(7 -> 2 -> 4 -> 3) 转为数字7243
- 然后将两个数字加起来得到和
- 将和转为字符串，字符串的没一个值即为链表中的一个结点数值

[代码实现](solution1.py)：
```py
class Solution:
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        p1 = l1
        while p1:
            num1 = num1 * 10 + p1.val
            p1 = p1.next
        num2 = 0
        p2 = l2
        while p2:
            num2 = num2 * 10 + p2.val
            p2 = p2.next
        
        str_sum = str(num1 + num2)
        p_result = ListNode(0)
        p_curr = p_result
        for item in str_sum:
            p_curr.next = ListNode(int(item))
            p_curr = p_curr.next
        return p_result.next
```