package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FourSum {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 4) {
            return res;
        }
        Arrays.sort(nums);

        int len = nums.length;
        int max = nums[len - 1];
        if (4 * nums[0] > target || 4 * max < target) {
            return res;
        }
        int i, z;
        for (i = 0; i < len; i++) {
            z = nums[i];
            if (i > 0 && z == nums[i -1]) continue;
            if (z + 3 * max < target) continue;
            if (4 * z > target) break;
            if (4 * z == target) {
                if (i + 3 < len && nums[i + 3] == z) {
                    res.add(Arrays.asList(z, z, z, z));
                }
                break;
            }
            threeSumForFourSum(nums, i + 1, len - 1, res, target - z, z);
        }
        return res;
    }

    private void threeSumForFourSum(int[] nums, int low, int high, List<List<Integer>> fourSumList, int target, int z1) {
        if (low + 1 >= high) return;
        int max = nums[high];
        if (3 * nums[low] > target || 3 * max < target) {
            return;
        }

        for (int i = low; i < high - 1; i++) {
            int z = nums[i];
            if (i > low && z == nums[i - 1]) {
                continue;
            }
            if (z + 2 * max < target) {
                continue;
            }
            if (3 * z > target) {
                break;
            }

            if (3 * z == target) {
                if (i + 1 < high && nums[i + 2] == z) {
                    fourSumList.add(Arrays.asList(z1, z, z, z));
                }
                break;
            }
            twoSumForFourSum(nums, i + 1, high, fourSumList, target - z, z1, z);
        }
    }

    private void twoSumForFourSum(int[] nums, int low, int high, List<List<Integer>> fourSumList, int target, int z1, int z2) {
        if (low >= high) return;
        if (2 * nums[low] > target || 2 * nums[high] < target) {
            return;
        }
        while (low < high) {
            int sum = nums[low] + nums[high];
            if (sum == target) {
                fourSumList.add(Arrays.asList(z1, z2, low, high));
                while (++low < high && nums[low] == nums[low + 1]);
                while (low < --high && nums[high] == nums[high - 1]);
            }
            if (sum < target) {
                low++;
            } else {
                high--;
            }
        }
    }

    public List<List<Integer>> fourSum1(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 4) {
            return result;
        }

        Arrays.sort(nums);

        int len = nums.length;
        int max = nums[len - 1];
        if (4 * nums[0] > target || 4 * max < target) {
            return result;
        }

        for (int i = 0; i < len - 3; i++) {
            if (4 * nums[i] > target) break;
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int z1 = nums[i];
            for (int j = i + 1; j < len - 2; j++) {
                if (z1 + 3 * nums[j] > target) break;
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                int z2 = nums[j];
                int low = j + 1;
                int high = len - 1;
                while (low < high) {
                    int sum = nums[low] + nums[high];
                    if (z1 + z2 + sum == target) {
                        result.add(Arrays.asList(z1, z2, nums[low], nums[high]));
                        int lowResult = nums[low];
                        int highResult = nums[high];
                        while (++low < high && nums[low] == lowResult);
                        while (low < --high && nums[high] == highResult);
                    } else if (z1 + z2 + sum < target) {
                        low++;
                    } else {
                        high--;
                    }
                }
            }
        }

        return result;
    }
}
