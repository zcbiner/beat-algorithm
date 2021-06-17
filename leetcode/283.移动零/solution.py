#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = -1
        end = 0
        while end < len(nums):
            if nums[end] != 0:
                start += 1
                nums[start] = nums[end]
            end += 1
        start += 1
        while start < len(nums):
            nums[start] = 0
            start += 1
# @lc code=end

