#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
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

# @lc code=end

