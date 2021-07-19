### 题目

> [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/description/)

假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**注意：**给定 *n* 是一个正整数。

**示例 1：**

```
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
```

**示例 2：**

```
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```

### 解题

n阶才能到楼顶，那我如何达到第n阶呢？只有两种情况：

1. 到达了n-1阶，我再爬1阶即可
2. 到达了n-2阶，我再爬2阶

动态规划题目。dp[n]表示达到第n阶有多少种情况，很显然`dp[n] = dp[n-1] + dp[n-2]`，当 n 小于等于2时，为其本身。自底向上遍历，得出dp[n]的值。

[代码实现：](solution.py)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0,1,2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
```

