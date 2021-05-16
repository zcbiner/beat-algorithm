### 题目
> [长度最小的子数组.](https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/)


给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：
```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```
示例 2：
```
输入：target = 4, nums = [1,4,4]
输出：1
```
示例 3：
```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

提示：
- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105
 
进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

### 解题

使用滑动窗口解题。

start和end包含的为子串，当子串内的和大于target时即满足了题目要求，更新result。

然后缩小滑动窗口的大小: start+=1。继续比较。

[代码实现：](solution.py)
```python
import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start和end分别为滑动窗口的左右指针
        start = end = 0

        result = sys.maxsize
        sum = 0
        while end < len(nums):
            sum += nums[end]
            # sum>=target说明当前窗口内的子串满足条件
            while sum >= target:
                length = end - start + 1
                if length < result:
                    result = length
                
                sum -= nums[start]
                start += 1
            end += 1
        if result == sys.maxsize:
            return 0
        else:
            return result
```