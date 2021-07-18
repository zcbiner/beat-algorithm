### 题目

> [二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/)

给定一个二叉树，返回它的 *后序* 遍历。

**示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

### 解题

#### 1.递归

so easy！

[代码实现：](solution.py)

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._traversal(root, res)
        return res

    def _traversal(self, root: TreeNode, res: List[int]):
        if not root:
            return
        
        self._traversal(root.left, res)
        self._traversal(root.right, res)
        res.append(root.val)
```

#### 2.迭代

迭代还相当不好理解，[代码如下：](solution1.py)

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
```

将根节点入栈，然后分别左右子树入栈，由于栈的特性，res最终放入了根节点、右子树、左子树。反转res，得到左子树、右子树、根节点，实现左右根的后序遍历。

还有一种解法是，每次都将访问节点放到结果列表的首位。[代码实现：](solution2.py)

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res
```

