#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            n_sum = numbers[left] + numbers[right]
            if n_sum < target:
                left += 1
            elif n_sum > target:
                right -= 1
            else :
                # 题目描述下标是从1开始的，而操作时是从0开始，所以要加1.
                return [left + 1, right + 1]
# @lc code=end

