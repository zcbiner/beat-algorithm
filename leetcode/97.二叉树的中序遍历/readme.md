### 题目
> [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/)

给定一个二叉树的根节点 `root` ，返回它的 **中序** 遍历。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
输入：root = [1,null,2,3]
输出：[1,3,2]
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
输出：[2,1]
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

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

### 解题

#### 1.递归解题

中序遍历，即先遍历左子树，再遍历根节点，最后遍历右子树。

[代码实现：](solution.py)

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result_list = []
        self._traversal(root, result_list)
        return result_list

    def _traversal(self, root: TreeNode, result_list: List[int]):
        if not root:
            return
        
        self._traversal(root.left, result_list)
        result_list.append(root.val)
        self._traversal(root.right, result_list)
```

#### 2.迭代解题

递归解题代码相当简单，那么如何使用迭代解题呢？递归的实质是借用了方法的调用栈，那么迭代解题可以使用自己的栈来处理。

[代码实现：](solution1.py)

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        temp_root = root
        result_list = []
        stack = []
        while True:
            while temp_root:
                stack.append(temp_root)
                temp_root = temp_root.left
            
            if len(stack) == 0:
                return result_list
            
            node = stack.pop()
            result_list.append(node.val)
            temp_root = node.right
```

