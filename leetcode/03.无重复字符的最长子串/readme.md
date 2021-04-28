### 题目
> [无重复字符的最长子串.](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/)

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：
- 0 <= s.length <= 5 * 104
- s 由英文字母、数字、符号和空格组成

### 解题
如果 s = "abcabcbb"，如何找出最长子串呢？
既然是子串那么肯定是在原有字符串中进行截取，而滑动窗口可以很好的解决问题。

左指针指向子串开始位置，右指针指向结束位置。向右移动指针，要保证左右指针间的子串没有重复的元素。
而为了保证没有重复元素，将滑动窗口中的元素都添加到set中，右指针滑动时判断是否重复，不重复继续滑动，否则终止。

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ans = 0
        # 滑动窗口的右指针
        right = -1
        sSize = len(s)
        # i为左指针
        for i in range(sSize):
            # 左指针向前加1，就需要移除之前左指针的字符
            if i > 0:
                charSet.remove(s[i - 1])
            # 滑动窗口右移
            while right + 1 < sSize and s[right + 1] not in charSet:
                right += 1
                charSet.add(s[right])
            ans = max(ans, right - i + 1)
        return ans
```

