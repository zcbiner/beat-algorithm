### 题目
> [比较含退格的字符串.](https://leetcode-cn.com/problems/backspace-string-compare/description/)


给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
```
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
```
示例 2：
```
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
```
示例 3：
```
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
```
示例 4：
```
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
```
 

提示：
- 1 <= S.length <= 200
- 1 <= T.length <= 200
- S 和 T 只含有小写字母以及字符 '#'。
 

进阶：
你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

### 解题

思路：使用双指针法。

如果从字符串的尾部开始遍历，遇到#也是删除#前面的一个字符，不会影响尾部字符。
因此从尾部开始遍历字符串。这里有三种情况：
1. 当遇到了#，则s_skip += 1标明下一个字符是要被删除的，要跳过。s_right -= 1也跳过当前的字符。
2. 当s_skip>0说明之前遇到了#，则当前字符是要被删除的，因此s_right -= 1，并将s_skip -= 1。
3. 说明当前字符是保留的，需要跟另一个字符串同等位置的字符进行比较。


[代码实现：](solution.py)
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_right = len(s) - 1
        s_skip = 0
        t_right = len(t) - 1
        t_skip = 0
        while s_right >= 0 or t_right >= 0:
            while s_right >= 0:
                if s[s_right] == '#':
                    s_skip += 1
                    s_right -= 1
                elif s_skip > 0:
                    s_skip -= 1
                    s_right -= 1
                else :
                    break
            
            while t_right >= 0:
                if t[t_right] == '#':
                    t_skip += 1
                    t_right -= 1
                elif t_skip > 0:
                    t_skip -= 1
                    t_right -= 1
                else :
                    break
            
            if s_right >= 0 and t_right >= 0:
                if s[s_right] != t[t_right]:
                    return False
            elif s_right >= 0 or t_right >= 0:
                return False
            
            s_right -= 1
            t_right -= 1
        
        return True
```