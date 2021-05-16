#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.search(nums, left, right, target)
    
    def search(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return left
        
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
        return self.search(nums, left, right, target)
# @lc code=end