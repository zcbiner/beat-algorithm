### 题目
> [移除元素。](https://leetcode-cn.com/problems/remove-element/description/)


给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
``` 

示例 1：
```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
```
示例 2：
```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
```

提示：
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

### 解题

与[26.删除有序数组中的重复项](../26.删除有序数组中的重复项/readme.md)是同一种类型的题目。思路也差不多一致。

[代码实现](solution.py)：
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        size = len(nums)
        l = 0
        r = 0
        while r < size:
            while r < size and nums[r] == val:
                r += 1
            if r >= size:
                break
            nums[l] = nums[r]
            l += 1
            r += 1
        return l
```

LeetCode的top voted解法，思路是将重复的元素移到数组尾部，很符合题目要求。
[代码实现](solution1.py):
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                end -= 1
            else:
                start += 1
        return start
```