#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        size = len(nums)
        l = 0
        r = 0
        while r < size:
            # 找到与nums[l]不相等的数
            while r < size and nums[r] == nums[l]:
                r += 1
            if r < size and l + 1 < r:
                nums[l + 1] = nums[r]
            l += 1
        return l
# @lc code=end

