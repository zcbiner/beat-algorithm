### 题目
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
```
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
```

示例 2：
```
输入：head = [0,1,2], k = 4
输出：[2,0,1]
```

提示：
- 链表中节点的数目在范围 [0, 500] 内
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109

### 解题
先理解题目。这里假设链表有环的话，就是把所有的节点都往右移动k个位置，然而这里是单链表。

但是我能不能先把单链表连接成环，移动完成后，再把环断开，这也达到了题目要求，而且很容易理解。

这里需要注意几个点：
- 如果k比链表的长度要长，说明绕了圈，需要求余
- 注意k=0，k=list_size以及链表为空，链表结点少于两个的情况
- 最后需要切断环

代码实现：[solution.py](solution.py):
```py
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0 or not head.next:
            return head
        p = head
        list_size = 1
        while p.next:
            p = p.next
            list_size = list_size + 1
        
        if k == list_size:
            return head
        # 头结点和尾结点相连，形成环
        p.next = head
        # k大于结点数，大于的部分是绕了一圈
        while k > list_size:
            k = k % list_size
        pre = head
        for i in range(list_size - k - 1):
            pre = pre.next
        
        head = pre.next
        # 切断环
        pre.next = None
        return head
```