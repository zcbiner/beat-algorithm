package sort;

/**
 * Created by zhong on 2017/9/23.
 * 归并排序
 */
public class MergeSort implements ISort {

    @Override
    public int[] sort(int[] list) {
        int[] a = new int[list.length];
        System.arraycopy(list, 0, a, 0, list.length);

        long time = System.currentTimeMillis();
        mergeSort(a, 0, a.length - 1);
        System.out.println("归并排序时间：" + (System.currentTimeMillis() - time));
        return a;
    }


    private void mergeSort(int[] a, int low, int high) {
        int mid = (low + high) / 2;
        if (low < high) {
            mergeSort(a, low, mid);
            mergeSort(a, mid + 1, high);
            merge(a, low, mid, high);
        }
    }

    private void merge(int[] a, int low, int mid, int high) {
        int[] temp = new int[high - low + 1];
        int i = low;
        int j = mid + 1;
        int k = 0;

        while (i <= mid && j <= high) {
            if (a[i] < a[j]) {
                temp[k++] = a[i++];
            } else {
                temp[k++] = a[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = a[i++];
        }

        while (j <= high) {
            temp[k++] = a[j++];
        }

        System.arraycopy(temp, 0, a, low, temp.length);
    }

}
