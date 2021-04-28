#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
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
# @lc code=end

