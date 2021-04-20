> 题目：[寻找两个正序数组的中位数。](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/)

### 解题
两个数组都是从小到大排序好的，那我可以将两个数组合并成一个，然后在一个有序的数组来找中位数就是一件很简单的事情了。

代码实现:
```py
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
```