### 题目
> [最长回文子串.](https://leetcode-cn.com/problems/longest-palindromic-substring/description/)

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

示例 2：
```
输入：s = "cbbd"
输出："bb"
```

示例 3：
```
输入：s = "a"
输出："a"
```

示例 4：
```
输入：s = "ac"
输出："a"
```
 

提示：
- 1 <= s.length <= 1000
- s 仅由数字和英文字母（大写和/或小写）组成

### 解题

仔细观察，回文子串的特性是对应位置的字符是相等的。这里有两种情况，一种单数，即aba这种情况，一种是偶数，aa这种情况。
因此这里分两步来判断。

[代码实现：](solution.py)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for index in range(len(s)):
            # 检查bccb这种情况
            temp = self.check(s, index, index + 1)
            if len(temp) > len(ans):
                ans = temp
            
            # 检查aba这种情况
            temp = self.check(s, index - 1, index + 1)
            if len(temp) > len(ans):
                ans = temp
        return ans
    
    def check(self, s, l, r):
        s_len = len(s)
        while l >= 0 and r < s_len and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
```