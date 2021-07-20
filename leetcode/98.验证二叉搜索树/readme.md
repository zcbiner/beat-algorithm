### 题目

> [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/description/)

给定一个二叉树，判断其是否是一个有效的二叉搜索树。假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含**小于**当前节点的数。
- 节点的右子树只包含**大于**当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1:**

```
输入:
    2
   / \
  1   3
输出: true
```

**示例 2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

### 解题

#### 1.递归

思路：对二叉搜索树进行中序遍历（先访问左子树，再访问根节点，最后访问右子树）。如果是二叉搜索树，那么中序遍历后得到的数组就是排序好的数组。

[代码实现：](solution.py)

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        val_list = []
        self._in_order(root, val_list)
        size = len(val_list)
        for i in range(1, size):
            if val_list[i - 1] >= val_list[i]:
                return False
        return True

    def _in_order(self, node: TreeNode, val_list: List[int]):
        if not node:
            return
        self._in_order(node.left, val_list)
        val_list.append(node.val)
        self._in_order(node.right, val_list)
```

#### 2.迭代

上面是通过递归进行中序遍历的，用迭代实现一遍。在迭代过程中，记录上一个结点的值：``pre_val``，然后使用这个值跟当前结点的值进行比较，如果前一个结点值大于等于当前结点值，说明不是二叉搜索树。迭代的解法好处是只用一次循环即完成了工作，时间复杂度为O(n)。另外只用到了一个栈进行辅助，空间复杂度为O(n)。

[代码实现：](solution1.py)

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        node = root
        pre_val = None
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            if len(stack) == 0:
                return True
            
            curr_node = stack.pop()
            if pre_val is not None and pre_val >= curr_node.val:
                return False
            pre_val = curr_node.val
            node = curr_node.right
```

