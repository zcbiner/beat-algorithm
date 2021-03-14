class BubbleSort {

    fun sort(nums: IntArray) {
        for (i in nums.indices) {
            for (j in i until (nums.size - 1)) {
                if (nums[j] > nums[j + 1]) {
                    val temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                }
            }
        }
    }
}