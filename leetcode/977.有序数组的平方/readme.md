### 题目

> [有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/)

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：

```
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```

示例 2：

```
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
```


提示：

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 已按 非递减顺序 排序


进阶：

- 请你设计时间复杂度为 O(n) 的算法解决本问题

### 解题

#### 双指针解题

使用双指针法，将数组划分为两部分。left部分为负数，right部分为大于0的数。

1. 每次都从left和right中取值，比较哪边的数较小。
2. 如果left小于0了，则只从right部分取值即可
3. 桶里如果right大于了数组长度，从left部分取值即可



[代码实现：](solution.py)

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        # 将数组划分为正负两部分
        while right < len(nums):
            if nums[right] >= 0:
                break
            right += 1
        left = right - 1

        ans = []
        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                a = nums[left] * nums[left]
                b = nums[right] * nums[right]
                if a > b:
                    ans.append(b)
                    right += 1
                else :
                    ans.append(a)
                    left -= 1
            elif left >= 0:
                ans.append(nums[left] * nums[left])
                left -= 1
            else :
                ans.append(nums[right] * nums[right])
                right += 1
        return ans
```

#### 排序算法解题

如果可以直接使用排序算法，那代码将变得相当简单，直接平方后排序即可。

[代码实现：](solution1.py)

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
```

