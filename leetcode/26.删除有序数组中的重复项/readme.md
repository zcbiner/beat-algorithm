### 题目
> [删除有序数组中的重复项。](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/)

给你一个有序数组 nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
 
示例 1：
```
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

示例 2：
```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
```

提示：
- 0 <= nums.length <= 3 * 104
- -104 <= nums[i] <= 104
- nums 已按升序排列

### 解题

比较简单的题目，双指针解题。

#### 思路
左指针指向已经合法的数据，右指针指向需要判断是否合法的数据。如果右指针的数据与左指针一样说明是需要删除的，跳过；如果不一样，说明是要保留的，左指针加1，将数据赋予左指针指向的数组位置。
[代码实现：](solution.py)
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        size = len(nums)
        l = 0
        r = 0
        while r < size:
            # 找到与nums[l]不相等的数
            while r < size and nums[r] == nums[l]:
                r += 1
            if r < size and l + 1 < r:
                nums[l + 1] = nums[r]
            l += 1
        return l
```

#### 优化解法
看到LeetCode的top voted解法，真的简洁很多。
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(len(nums) - 1):
            if nums[r] != nums[r + 1]:
                nums[l] = nums[r + 1]
                l += 1
        return l
```