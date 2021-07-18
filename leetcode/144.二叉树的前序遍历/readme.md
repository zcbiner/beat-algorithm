### 解题

> [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/)

给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
输入：root = [1,null,2,3]
输出：[1,2,3]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

**示例 4：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)

```
输入：root = [1,2]
输出：[1,2]
```

**示例 5：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
输入：root = [1,null,2]
输出：[1,2]
```

**提示：**

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

**进阶：**递归算法很简单，你可以通过迭代算法完成吗？

### 解题

#### 1.递归

so easy！

[代码实现：](solution.py)

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._traversal(root, res)
        return res

    def _traversal(self, root: TreeNode, res: List[int]):
        if not root:
            return
        res.append(root.val)
        self._traversal(root.left, res)
        self._traversal(root.right, res)
```

#### 2.迭代

迭代的解法，需要好好理解。前序遍历是先访问根节点，访问根节点后，要先入栈右子树再入栈左子树。因为pop时，会将后入栈的弹出。

[代码实现：](solution1.py)

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node= stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```

