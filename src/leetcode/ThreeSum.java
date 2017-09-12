package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
public class ThreeSum {

    public static List<List<Integer>> solution(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> lists = new ArrayList<>();
        int mid, right;
        for (int left = 0; left < nums.length - 2; left++) {
            if (left > 0 && nums[left] == nums[left - 1]) {
                continue;
            }
            mid = left + 1;
            right = nums.length - 1;
            int sum = 0 - nums[left];
            while (mid < right) {
                int result = nums[mid] + nums[right];
                if (result == sum) {
                    lists.add(Arrays.asList(nums[left], nums[mid], nums[right]));
                    mid++;
                    right--;
                    while (mid < right && nums[mid] == nums[mid - 1]) mid++;
                    while (mid < right && nums[right] == nums[right + 1]) right--;
                } else if (result > sum) {
                    right--;
                } else {
                    mid++;
                }
            }
        }
        return lists;
    }
}
