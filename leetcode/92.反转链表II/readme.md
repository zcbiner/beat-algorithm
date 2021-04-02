### 题目
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 
示例 1：
```
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
```

示例 2：
```
输入：head = [5], left = 1, right = 1
输出：[5]
```

提示：
- 链表中节点数目为 n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

进阶： 你可以使用一趟扫描完成反转吗？

### 解题
如何翻转链表结点呢？就是把当前结点的指针指向前一个结点。代码如下：
```py
#p_curr表示当前遍历结点
#p_curr_after表示p_curr的下一个结点
#p_curr_pre表示p_curr的前一个结点
while p_curr:
    p_curr_after = p_curr.next
    p_curr = p_curr_pre
    p_curr_pre = p_curr
    p_curr = p_curr_after
```
在翻转的时候注意不要丢了结点。

在这道题中，我只要翻转left到right的结点就行了。翻转完后处理下left和right这两个结点的指向，题目就完成了。

代码实现:[solution.py](solution.py)
我的解题方法中指针比较多，主要是为了满足一趟扫描完成反转，需要注意每个指针的含义。注释都已经写了。