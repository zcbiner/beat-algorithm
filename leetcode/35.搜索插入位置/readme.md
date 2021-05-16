### 题目
> [搜索插入位置.](https://leetcode-cn.com/problems/search-insert-position/description/)


给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:
```
输入: [1,3,5,6], 5
输出: 2
```
示例 2:
```
输入: [1,3,5,6], 2
输出: 1
```
示例 3:
```
输入: [1,3,5,6], 7
输出: 4
```
示例 4:
```
输入: [1,3,5,6], 0
输出: 0
```

### 解题

排序数组找索引，肯定是二分法了。

[代码实现：](solution.py)
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        # 如果while循环中没有找到，说明数组中没有这个值。
        # 此时的left即为要插入的位置
        return left
```

上面是while循环的解法，当然还可以写成递归的形式：
[代码实现:](solution1.py)
```python
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
```