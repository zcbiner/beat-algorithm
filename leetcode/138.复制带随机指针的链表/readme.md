> 题目：[复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/)

### 解题
本题说白了就是要复制一个跟原链表一样的链表，而难点在于有随机指针。

参考解题：https://zhuanlan.zhihu.com/p/100388274

[代码实现](solution.py)：
```py
class Solution:

    # 初始化一个map
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = Node(head.val, None, None)
        self.visitedHash[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
```