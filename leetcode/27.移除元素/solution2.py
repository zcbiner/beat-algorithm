#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       slow = 0
       fast = 0
       for fast in range(len(nums)):
           if nums[fast] != val:
               nums[slow] = nums[fast]
               slow += 1
        
       return slow
# @lc code=end