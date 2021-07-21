### 题目

> [二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/)

给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其自底向上的层序遍历为：

```
[
  [15,7],
  [9,20],
  [3]
]
```

### 解题

这里就是一个二叉树的层序遍历，可以参考：[102.二叉树的层序遍历](../102.二叉树的层序遍历/readme.md)，那么本题就是在层序遍历的基础上，将结果列表进行翻转。

[代码实现：](solution.py)

```pytho
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            temp_list = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp_list)
        return res[::-1]
```

为了不在最后多一次翻转的循环，可以在每次遍历时，将每层的遍历结果放到`res`的第一个位置。

[代码实现：](solution1.py)

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            temp_list = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, temp_list)
        return res
```

