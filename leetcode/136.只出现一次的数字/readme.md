### 题目
[只出现一次的数字](https://leetcode-cn.com/problems/single-number/description/)

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
```
输入: [2,2,1]
输出: 1
```

示例 2:
```
输入: [4,1,2,1,2]
输出: 4
```

### 解题
#### hash解法
刚看到题目的时候，其实想到的就是Hash。
因为Hash很好解决这种次数问题。
- 先遍历数组，将每个数字的出现次数保存到map中。
- 再次遍历数组，返回次数为1的数。

解法实现：
```kotlin
class Solution {
    fun singleNumber(nums: IntArray): Int {
        val hashMap = mutableMapOf<Int, Int>()
        for (i in nums.indices) {
            var count = hashMap.get(nums[i])
            if (count == null) {
                count = 0
            }
            count++
            hashMap.put(nums[i], count)
        }
        for (i in nums.indices) {
            if (hashMap.get(nums[i]) == 1) {
                return nums[i]
            }
        }
        return -1
    }
}
```
#### 异或解法
然而题目可是有明确要求的：你可以不使用额外空间来实现吗？
第一种解法的时间复杂度是2n即O(n)，空间复杂度O(n)。没有达成题目要求。

我还是看他人的解法看到可以用异或这种巧妙的解法的，难怪本题被标明为easy。
异或的特性：
1. 交换律：a ^ b ^ c <=> a ^ c ^ b
2. 任何数于0异或为任何数 0 ^ n => n
3. 相同的数异或为0: n ^ n => 0

下面是本题解法：
```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```