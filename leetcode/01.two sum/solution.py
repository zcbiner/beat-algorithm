#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i, value in enumerate(nums):
            diff = target - nums[i]
            if diff in mapping:
                return [mapping[diff], i]
            else:
                mapping[value] = i
# @lc code=end