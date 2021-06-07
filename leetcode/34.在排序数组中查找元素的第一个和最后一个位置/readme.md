### 题目
> [在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
```
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```

示例 2：
```
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```

示例 3：
```
输入：nums = [], target = 0
输出：[-1,-1]
```
 

提示：
- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109
- nums 是一个非递减数组
- -109 <= target <= 109

### 解题

二分法找到与target相等的数，然后再往左右遍历找到起始位置。

[代码实现](solution.py)
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2 
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                start = middle
                end = middle
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                ans[0] = start + 1
                ans[1] = end - 1
                break
        return ans
```