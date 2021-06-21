#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
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
# @lc code=end

