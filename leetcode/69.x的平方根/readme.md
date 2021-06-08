### 题目
> [x 的平方根](https://leetcode-cn.com/problems/sqrtx/description/)

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
```
输入: 4
输出: 2
```

示例 2:
```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

### 解题

使用二分法找到一个数middle，如果middle*middle=x说明middle是平方根。
然而存在一种情况是x的平方根不是整数，所以如果x在middle*middle和(middle + 1)*(middle + 1)之间，这个middle也是满足条件的。

[代码实现：](solution.py)
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x
        while left <= right:
            middle = left + (right - left) // 2
            temp = middle * middle
            if temp <= x < (middle + 1) * (middle + 1):
                return middle
            elif temp > x:
                right = middle - 1
            else :
                left = middle + 1
        return left
```