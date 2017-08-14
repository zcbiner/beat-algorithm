package sort;

import java.util.Random;

/**
 * Created by zhong on 2017/8/5.
 */
public class MainSort {
    public static void main(String[] args) {
        int[] a = generateData(1000);
        ISort iSorta = new BubbleSort();
        printIntArray(iSorta.sort(a), "冒泡");

        ISort iSortb = new QuickSort();
        printIntArray(iSortb.sort(a), "快速");

        ISort iSortc = new SelectSort();
        printIntArray(iSortc.sort(a), "选择");

        ISort iSortd = new InsertSort();
        printIntArray(iSortd.sort(a), "插入");

        ISort iSorte = new ShellSort();
        printIntArray(iSorte.sort(a), "希尔");

        ISort iSortf = new HeapSort();
        printIntArray(iSortf.sort(a), "堆");
    }

    public static int[] generateData(int length) {
        int[] a = new int[length];
        System.out.print("原始数据：");
        for (int i = 0; i < length; i++) {
            a[i] = new Random().nextInt(20000);
            System.out.print(a[i] + " ");
        }
        System.out.println();
        return a;
    }

    public static void printIntArray(int[] a, String sortName) {
        System.out.print(sortName + "排序后数据：");
        for (int i : a) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
