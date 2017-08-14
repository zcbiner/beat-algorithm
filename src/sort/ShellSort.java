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
        int gap = a.length / 3 + 1;
        while (gap > 1) {
            for (int i = 0; i < a.length - gap; i++) {
                if (a[i] > a[i + gap]) {
                    int temp = a[i];
                    a[i] = a[i + gap];
                    a[i + gap] = temp;
                }
            }
            gap = gap / 3 + 1;
        }
        System.out.println("希尔排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }
}
