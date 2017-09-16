package sort;

/**
 * Created by zhong on 2017/8/5.
 * 希尔排序
 */
public class ShellSort implements ISort {

    @Override
    public int[] sort(int[] list) {

        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);

        long time = System.currentTimeMillis();
        int gap = a.length / 2;
        while (gap >= 1) {
            for (int i = gap; i < a.length; i++) {
                int temp = a[i];
                int j = i - gap;
                while (j >= 0 && a[j] > temp) {
                    a[j + gap] = a[j];
                    j -= gap;
                }
                a[j + gap] = temp;
            }
            gap = gap / 2;
        }
        System.out.println("希尔排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }
}
