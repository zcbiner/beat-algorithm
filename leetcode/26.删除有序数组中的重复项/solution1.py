#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(len(nums) - 1):
            if nums[r] != nums[r + 1]:
                nums[l] = nums[r + 1]
                l += 1
        return l
# @lc code=end

