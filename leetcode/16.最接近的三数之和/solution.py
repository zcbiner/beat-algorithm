#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # 相等最接近，直接返回
                if s == target:
                    return target

                if abs(s - target) < abs(ans - target):
                    ans = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return ans

# @lc code=end

