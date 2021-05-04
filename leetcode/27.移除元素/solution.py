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
        size = len(nums)
        l = 0
        r = 0
        while r < size:
            while r < size and nums[r] == val:
                r += 1
            if r >= size:
                break
            nums[l] = nums[r]
            l += 1
            r += 1
        return l
# @lc code=end