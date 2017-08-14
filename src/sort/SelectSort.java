package sort;

/**
 * Created by zhong on 2017/8/5.
 * 核心：不断地选择剩余元素中的最小者。
 * 1. 找到数组中最小元素并将其和数组第一个元素交换位置。
 * 2. 在剩下的元素中找到最小元素并将其与数组第二个元素交换，直至整个数组排序。
 * 最大特点是交换移动数据次数相当少。
 * 时间复杂度O(n*n)
 */
public class SelectSort implements ISort {

    @Override
    public int[] sort(int[] list) {

        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);

        long time = System.currentTimeMillis();
        for (int i = 0; i < a.length; i++) {
            int minIndex = i;
            for (int j = i; j < a.length; j++) {
                if (a[minIndex] > a[j]) {
                    minIndex = j;
                }
            }
            int temp = a[minIndex];
            a[minIndex] = a[i];
            a[i] = temp;
        }
        System.out.println("选择排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }
}
