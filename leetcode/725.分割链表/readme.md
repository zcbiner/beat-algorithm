> 题目：[分割链表。](https://leetcode-cn.com/problems/split-linked-list-in-parts/description/)

### 解题
将链表分为k个连续部分，其中要注意：
- 每部分的长度尽可能相等
- 任意两部分的长度差距不能超过1，可能有部分为null
- 排在前面的部分的长度应该大于或等于后面的长度

遍历获取到链表结点长度node_size，要将node_size分为k份，因此node_size 除以 k得到count为每份的长度。
而有可能node_size除以k不能整除，求得余数remainder。题目的要求：
- 任意两部分的长度差距不能超过1，可能有部分为null
- 排在前面的部分的长度应该大于或等于后面的长度

所以如果余数大于0，那么它应该在第一部分多分配一个，余数减一，第二部分多分配一个，余数再减一，依次类推。

[代码实现](solution.py)：
```py
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        p_curr = root
        node_size = 0
        while p_curr:
            node_size += 1
            p_curr = p_curr.next
        count = node_size // k
        remainder = node_size % k
        result = []
        p_curr = root
        # 分割成k部分
        for i in range(k):
            split_size = count
            if remainder > 0:
                split_size += 1
                remainder -= 1
            new_head = p_curr
            # 找到分割的前一个结点
            while split_size > 1 and p_curr:
                split_size -= 1
                p_curr = p_curr.next
            if p_curr:
                p_temp = p_curr
                p_curr = p_curr.next
                p_temp.next = None
            result.append(new_head)
        return result
```
没有太多花里胡哨的操作，感觉就是考察算法基本功。竟然一次就AC了，说明解题有所进步了。