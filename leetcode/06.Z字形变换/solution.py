#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
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

# @lc code=end

