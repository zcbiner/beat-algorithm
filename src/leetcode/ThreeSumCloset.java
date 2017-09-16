package leetcode;

import java.util.Arrays;

/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
public class ThreeSumCloset {

    public static int solution(int[] nums, int target) {
        Arrays.sort(nums);

        int min = nums[0] + nums[1] + nums[2];
        for (int left = 0; left < nums.length - 2; left++) {
            int mid = left + 1;
            int right = nums.length - 1;
            int temp = target - nums[left];
            while (mid < right) {
                int sum = nums[mid] + nums[right];
                if (Math.abs(temp - sum) < Math.abs(target - min)) {
                    min = nums[left] + nums[mid] + nums[right];
                }

                if (sum == temp) {
                    return target;
                } else if (sum < temp) {
                    mid++;
                } else {
                    right--;
                }
            }
        }

        return min;
    }
}
