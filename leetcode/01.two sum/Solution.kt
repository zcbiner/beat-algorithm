/*
 * @lc app=leetcode.cn id=1 lang=kotlin
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        for (i in 0..(nums.size - 1)) {
            map[nums[i]]?.let {
                return intArrayOf(it, i)
            }
            map[target - nums[i]] = i
        }
        return intArrayOf()
    }
}
// @lc code=end