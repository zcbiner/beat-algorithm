#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start和end分别为滑动窗口的左右指针
        start = end = 0

        result = sys.maxsize
        sum = 0
        while end < len(nums):
            sum += nums[end]
            while sum >= target:
                length = end - start + 1
                if length < result:
                    result = length
                
                sum -= nums[start]
                start += 1
            end += 1
        if result == sys.maxsize:
            return 0
        else:
            return result
# @lc code=end

