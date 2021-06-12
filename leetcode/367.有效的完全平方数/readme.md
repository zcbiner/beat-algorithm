### 题目
> [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/description/)


给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

示例 1：
```
输入：num = 16
输出：true
```

示例 2：
```
输入：num = 14
输出：false
```
 
提示：
- 1 <= num <= 2^31 - 1

### 解题
二分法找到一个数x，使得x*x=num。

[代码实现：](solution.py)
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            middle = left + (right - left) // 2
            if num == middle * middle:
                return True
            elif num < middle * middle:
                right = middle - 1
            else :
                left = middle + 1
        
        return False
```