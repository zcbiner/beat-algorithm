package sort;

/**
 * Created by zhong on 2017/8/5.
 * 快速排序之所以比较快，是因为相比冒泡排序，每次交换是跳跃式的。
 * 每次排序的时候设置一个基准点，将小于等于基准点的数全部放到基准点的左边，将大于等于基准点的数全
 * 部放到基准点的右边。这样在每次交换的时候就不会像冒泡排序一样只能在相邻的数之间进
 * 行交换，交换的距离就大得多了。因此总的比较和交换次数就少了，速度自然就提高了。当
 * 然在最坏的情况下，仍可能是相邻的两个数进行了交换。
 * 因此快速排序的最差时间复杂度和冒泡排序是一样的，都是 O(N*N)，它的平均时间复杂度为 O (NlogN)。
 */

public class QuickSort implements ISort {
    @Override
    public int[] sort(int[] list) {

        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);

        long time = System.currentTimeMillis();
        quickSort(a, 0, a.length - 1);
        System.out.println("快速排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }

    private void quickSort(int[] a, int left, int right) {
        if (left > right) {
            return;
        }

        int i = left;
        int j = right;
        int temp = a[left];

        while (i != j) {

            while (a[j] >= temp && i < j) {
                j--;
            }

            while (a[i] <= temp && i < j) {
                i++;
            }

            if (i < j) {
                int t = a[j];
                a[j] = a[i];
                a[i] = t;
            }
        }

        a[left] = a[i];
        a[i] = temp;

        quickSort(a, left, i - 1);
        quickSort(a, i + 1, right);
    }
}
