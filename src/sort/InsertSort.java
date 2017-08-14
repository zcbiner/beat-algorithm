package sort;

/**
 * Created by zhong on 2017/8/5.
 * 插入排序
 * 将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表。
 * 时间复杂度O(n*n)。比冒泡和选择排序效率高
 */
public class InsertSort implements ISort {

    @Override
    public int[] sort(int[] list) {
        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);
        long time = System.currentTimeMillis();
        for (int i = 1; i < a.length; i++) {
            int temp = a[i];
            int j = i;
            for (; j > 0 && temp < a[j - 1]; j--) {
                a[j] = a[j - 1];
            }
            a[j] = temp;
        }
        System.out.println("插入排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }
}
