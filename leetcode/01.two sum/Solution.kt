class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = HashMap<Int, Int>()
        for (i in 0..(nums.size - 1)) {
            if (map.containsKey(nums[i])) {
                return intArrayOf(map[nums[i]]!!, i)
            }
            map[target - nums[i]] = i
        }
        return intArrayOf(-1, -1)
    }
}