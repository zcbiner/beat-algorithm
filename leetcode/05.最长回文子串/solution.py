#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
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
# @lc code=end
