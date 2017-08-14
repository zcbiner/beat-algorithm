package sort;

/**
 * Created by zhong on 2017/8/14.
 */
public class HeapSort implements ISort {
    @Override
    public int[] sort(int[] list) {
        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);
        long time = System.currentTimeMillis();
        for (int i = a.length / 2 - 1; i >= 0; i--) {
            maxHeap(a, i, a.length - 1);
        }

        for (int i = a.length - 1; i > 0; i--) {
            int temp = a[0];
            a[0] = a[i];
            a[i] = temp;
            maxHeap(a, 0, i - 1);
        }
        System.out.println("堆排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }

    // 构建最大堆
    private void maxHeap(int[] arr, int start, int end) {
        int dad = start;
        int son = dad * 2 + 1;
        while (son <= end) {
            // 子节点中较大的那个
            if (son + 1 <= end && arr[son] < arr[son + 1]) {
                son++;
            }

            if (arr[dad] > arr[son]) {
                return;
            } else {
                int temp = arr[dad];
                arr[dad] = arr[son];
                arr[son] = temp;
                dad = son;
                son = dad * 2 + 1;
            }
        }
    }
}
