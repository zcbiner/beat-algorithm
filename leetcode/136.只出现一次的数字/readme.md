### 思路

刚看到题目的时候，其实想到的就是Hash。
因为Hash很好解决这种次数问题。那么第一种解法其实就出来了：
```
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
然而题目可是有明确要求的：你可以不使用额外空间来实现吗？
第一种解法的时间复杂度是2n即O(n)，空间复杂度O(n)。没有达成题目要求。

我还是看他人的解法看到可以用异或这种巧妙的解法的，难怪本题被标明为easy。
异或的特性：

1. 交换律：a ^ b ^ c <=> a ^ c ^ b
2. 任何数于0异或为任何数 0 ^ n => n
3. 相同的数异或为0: n ^ n => 0


下面是本题解法：
```
class Solution {
    fun singleNumber(nums: IntArray): Int {
        var result = 0
        nums.forEach {
            result = result xor it
        }
        return result
    }
}
```