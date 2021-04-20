### 题目
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

示例 2：
```
输入：head = []
输出：[]
```

示例 3：
```
输入：head = [1]
输出：[1]
```

提示：
- 链表中节点的数目在范围 [0, 100] 内
- 0 <= Node.val <= 100

进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）

### 解题
这道题相对简单，没有看任何题解就做出来了。

#### 解法一

使用一个哨兵节点指向头结点能极大的简化问题，然后就是节点之间的操作，注意画图理解即可。
代码实现在[solution.py](solution.py)：
```py
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        p1 = head
        p2 = head.next
        while p1 is not None and p2 is not None:
            # 将p1，p2节点互换
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            # 更新pre，p1，p2指向节点，进行下一轮的互换
            pre = p1
            p1 = p1.next
            if p1 is None:
                break
            p2 = p1.next
            if p2 is None:
                break
        return dummy.next
```

### 解法二

但是我的代码虽然AC了，但是看起来比别人的相对复杂。注意到这个判断条件是可以简化的：
```py
while p1 is not None and p2 is not None
```
简化为：
```py
while pre.next and pre.next.next
```

就可以简化部分代码。实现在[solution1.py](solution1.py)：
```py
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            # p1，p2指向两个要交换的节点点
            p1 = pre.next
            p2 = pre.next.next
            # 进行交换
            pre.next = p2
            p1.next = p2.next
            p2.next = p1
            # 更新pre，进行下一轮替换
            pre = p1
        return dummy.next
````
