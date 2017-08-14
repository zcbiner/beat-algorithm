package sort;

/**
 * Created by zhong on 2017/8/5.
 * 冒泡排序的基本思想是：每次比较两个相邻的元素，如果它们的顺序错误就把它们交换过来。
 * 时间复杂度:O(n*n)
 */
public class BubbleSort implements ISort {

    @Override
    public int[] sort(int[] list) {
        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);
        long time = System.currentTimeMillis();
        if (a.length > 0) {
            for(int i = 0; i < a.length; i++) {
                for (int j = a.length - 1; j > i; j--) {
                    if (a[j] < a[j - 1]) {
                        int temp = a[j - 1];
                        a[j - 1] = a[j];
                        a[j] = temp;
                    }
                }
            }
        }
        System.out.println("冒泡排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }
}
