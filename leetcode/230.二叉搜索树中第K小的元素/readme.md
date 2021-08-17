### 题目

> [二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/)

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 个最小元素（从 1 开始计数）。

 
**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
输入：root = [3,1,4,null,2], k = 1
输出：1
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```

**提示：**

- 树中的节点数为 `n` 。
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？

### 思路
#### 先遍历再查找
二叉搜索树的中序遍历即为已排序集合。因此通过中序遍历获取排序好的值，再找到第`k`小的值。
[代码实现:](solution.py)
```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val_list = []
        self._traversal(root, k, val_list)
        return val_list[k - 1]

    def _traversal(self, root: TreeNode, k: int, val_list: List[int]):
        if not root:
            return -1
        
        self._traversal(root.left, k, val_list)
        val_list.append(root.val)
        self._traversal(root.right, k, val_list)
```
#### 优化解法
上面的解题方案是没有问题的，然而我们还可以减少空间复杂度以及减少遍历次数。
在遍历过程中，每遍历一次即减少k的值，当k==0时即为要找的元素。
[代码实现:](solution1.py)
```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self._traversal(root)
        return self.ans

    def _traversal(self, root: TreeNode):
        if not root:
            return
        
        self._traversal(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return
        self._traversal(root.right)
```