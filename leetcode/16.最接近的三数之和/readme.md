### 题目
> [最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/description/)

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
```
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```
 

提示：
- 3 <= nums.length <= 10^3
- -10^3 <= nums[i] <= 10^3
- -10^4 <= target <= 10^4

### 解题

与[15.三数之和](../15.三数之和/readme.md)是差不多的题目，只不过把等于0换成了最接近的和。处理思路一致，排序后就很好解决了。

[代码实现：](solution.py)
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # 相等最接近，直接返回
                if s == target:
                    return target

                if abs(s - target) < abs(ans - target):
                    ans = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return ans
```