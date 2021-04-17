#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 将两个数组合并成一个
        nums = []
        i = 0
        j = 0
        size1 = len(nums1)
        size2 = len(nums2)
        while i < size1 or j < size2:
            if i >= size1:
                nums.append(nums2[j])
                j += 1
            elif j >= size2:
                nums.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
        # 找到中点确定中位数
        middle = len(nums) // 2
        if (len(nums) % 2) == 0:
            return (nums[middle - 1] + nums[middle]) / 2
        else :
            return nums[middle]

# @lc code=end

