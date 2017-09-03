package leetcode;

import java.util.HashMap;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 */
public class TwoSum {

    public static int[] solution1(int[] nums, int target) {
        for (int i = 0; i < nums.length ; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if ((nums[i] + nums[j]) == target) {
                    return new int[]{i, j};
                }
            }
        }
        throw new IllegalArgumentException("no such result");
    }

    public static int[] solution2(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                return new int[]{map.get(nums[i]), i};
            }
            map.put(target - nums[i], i);
        }

        throw new IllegalArgumentException("no such result");
    }

    public static void main(String[] args) {
        int[] nums = new int[] {6, 0, 8, 9, 3, 11, 13, 4};
        int target = 10;

        int[] r1 = solution1(nums, target);
        int[] r2 = solution2(nums, target);
        System.out.println(r1[0] + " " + r1[1]);
        System.out.println(r2[0] + " " + r2[1]);
    }
}
