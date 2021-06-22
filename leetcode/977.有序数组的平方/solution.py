#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        # 将数组划分为正负两部分
        while right < len(nums):
            if nums[right] >= 0:
                break
            right += 1
        left = right - 1

        ans = []
        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                a = nums[left] * nums[left]
                b = nums[right] * nums[right]
                if a > b:
                    ans.append(b)
                    right += 1
                else :
                    ans.append(a)
                    left -= 1
            elif left >= 0:
                ans.append(nums[left] * nums[left])
                left -= 1
            else :
                ans.append(nums[right] * nums[right])
                right += 1
        return ans
# @lc code=end

