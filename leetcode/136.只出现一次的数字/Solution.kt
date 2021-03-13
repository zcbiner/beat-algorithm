/*
 * @lc app=leetcode.cn id=136 lang=kotlin
 *
 * [136] 只出现一次的数字
 */

// @lc code=start
class Solution {
    fun singleNumber(nums: IntArray): Int {
        var result = 0
        nums.forEach {
            result = result xor it
        }
        return result
    }
}
// @lc code=end

