#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
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
# @lc code=end

