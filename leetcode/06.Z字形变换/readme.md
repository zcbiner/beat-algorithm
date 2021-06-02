### 题目
> [Z 字形变换.](https://leetcode-cn.com/problems/zigzag-conversion/description/)

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

```
P   A   H   N
A P L S I I G
Y   I   R
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

```string convert(string s, int numRows);```


示例 1：

```输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```

示例 3：

```
输入：s = "A", numRows = 1
输出："A"
```


提示：

- 1 <= s.length <= 1000
- s 由英文字母（小写和大写）、',' 和 '.' 组成
- 1 <= numRows <= 1000

### 解题

仔细观察，发现字符可以按行读取。比如这个有一个字符为：PAYPALISHIRING，行数为3时，Z字形排列为：

```
P   A   H   N
A P L S I I G
Y   I   R
```

创建一个数组为row_array，大小为3。第0行存的字符应该是PAHN，第二行应该是APLSIIG，第三行为YIR。将每行依次连接依赖就是转换后的结果：PAHNAPLSIIGYIR。

因此在遍历字符串时，将字符依次放到第0，1，2行，放完后再递减，依次放到（2-1）行，(1-1)行，当行数为0时，又开始递增。

[代码实现：](solution.py)

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_size = len(s)
        if numRows == 1 or numRows >= s_size:
            return s
        
        row_array = [''] * numRows
        row = 0
        step = 1
        for c in s:
            row_array[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        
        return ''.join(row_array)
```



