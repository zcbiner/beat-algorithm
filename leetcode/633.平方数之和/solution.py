#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            s = l * l + r * r
            if s < c:
                l += 1
            elif s > c:
                r -= 1
            else :
                return True
        return False
                
# @lc code=end

