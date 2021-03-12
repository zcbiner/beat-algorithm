/*
 * @lc app=leetcode.cn id=239 lang=kotlin
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        if (nums == null || nums.size < 2) {
            return nums
        }
        val ans = IntArray(nums.size - k + 1)
        val deque = LinkedList<Int>()
        for (i in nums.indices) {
            while(deque.isNotEmpty() && deque.peekFirst() < (i + 1 - k)) {
                deque.removeFirst()
            }
            while(deque.isNotEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.removeLast()
            }
            deque.add(i)
            if (i >= k - 1) {
                ans[i + 1 - k] = nums[deque.peekFirst()]
            }
        }
        return ans
    }
}
// @lc code=end
