### 题目

> [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/)

给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。 

**示例：**
二叉树：`[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层序遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```

### 解题

思路：

1. 先将根节点入队列
2. 访问当前队列里的所有结点
3. 将当前队列里所有结点的子结点入队列

[代码实现：](solution.py)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        node_queue = [root]
        res = []
        while node_queue:
            level_list = []
            # 这里一定要根据当前队列的size来遍历，这个size表示属于当层的结点数。
            for i in range(len(node_queue)):
                node = node_queue.pop(0)
                level_list.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            res.append(level_list)
        return res
```

