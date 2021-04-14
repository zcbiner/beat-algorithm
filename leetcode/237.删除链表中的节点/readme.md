> 题目：[删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/description/)。

### 解题
仔细理解题目，给出的参数仅仅是要被删除的结点，不知道它的前一个结点，就没法使用常规的链表删除手段：``p.next = p.next.next``。

具体怎么做其实题目已经有提示了，注意这几点：
1. 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
2. 链表至少包含两个节点。
3. 链表中所有节点的值都是唯一的。

那么这里的删除其实是一个取巧手段：狸猫换太子。将下一个结点的值赋予当前结点，然后删除下一个结点。这样删除的其实是下一个结点，然而当前的结点替换成了下一个结点的值，达到了删除当前结点的效果。

[代码实现](solution.py)：
```py
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```
