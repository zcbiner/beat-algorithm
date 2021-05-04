#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                end -= 1
            else:
                start += 1
        return start
# @lc code=end