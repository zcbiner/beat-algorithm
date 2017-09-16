package leetcode;

public class MostWater {
    public int solution(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int i = height[left] > height[right] ? right : left;
        int vol;
        int volMax = height[i] * (right - left);
        while (left < right) {
            if (height[left] < height[right]) {
                left++;
            } else {
                right++;
            }

            vol = Math.min(height[left], height[right]) * (right - left);
            if (vol > volMax) volMax = vol;
        }
        return volMax;
    }
}
