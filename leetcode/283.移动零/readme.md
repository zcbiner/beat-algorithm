### 题目
> [移动零](https://leetcode-cn.com/problems/move-zeroes/description/)

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

说明:
- 必须在原数组上操作，不能拷贝额外的数组。
- 尽量减少操作次数。

### 解题

使用双指针实现，start指针之前的数据为已经移动没有0的数据，end指针用于寻找下一个非0数。最后start停留的位置已经将整个数组所有的非0数都移动过来了，所以start之后的数据全部置0即可。
[代码实现：](solution.py)
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = -1
        end = 0
        while end < len(nums):
            if nums[end] != 0:
                start += 1
                nums[start] = nums[end]
            end += 1
        start += 1
        while start < len(nums):
            nums[start] = 0
            start += 1
```

这里还有一个相当巧妙的解题方法。
[代码实现：](solution1.py)
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
```
怎么理解呢？zero表示为0的位置，每次都将非0的数与0交换位置。
