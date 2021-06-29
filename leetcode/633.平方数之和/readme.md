### 题目

> [平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/description/)

给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 `a2 + b2 = c` 。

 **示例 1：**

```
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
```

**示例 2：**

```
输入：c = 3
输出：false
```

**示例 3：**

```
输入：c = 4
输出：true
```

**示例 4：**

```
输入：c = 2
输出：true
```

**示例 5：**

```
输入：c = 1
输出：true 
```

**提示：**

- `0 <= c <= 231 - 1`

### 解题

从0到c中找到两个数a、b，使得``a*a + b*b=c``。所以左指针初始化为0.

右指针可以从c的平方根开始，减少循环次数。

[代码实现：](solution.py)

```python
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            s = l * l + r * r
            if s < c:
                l += 1
            elif s > c:
                r -= 1
            else :
                return True
        return False
```

