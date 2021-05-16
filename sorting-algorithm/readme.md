### 排序算法

O(n^2)的算法
   - 冒泡排序
   - 选择排序
   - 插入排序
   - 希尔排序
  
O(nlogn)的算法
   - 快速排序
   - 归并排序
   - 堆排序

### 一、冒泡排序

冒泡排序只会操作相邻的两个数据。

每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。如果不满足就让它俩互换。

一次冒泡会让至少一个元素移动到它应该在的位置，重复n次，就完成了n个数据的排序工作。

以下实现中，j从数组倒数第二数开始，进行比较：``if (arr[j] > arr[j + 1])``。如果前一个数大于后一个数，就交换位置。
这样数组中最小的数就到了0的位置，然后j更新为倒数第三个数，i更新为1，继续比较。

[代码实现：](src/bubble_sort.py)
```python
class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if (arr[j] > arr[j + 1]):
                    # swap arr[j] and arr[j + 1]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

### 二、选择排序
选择排序将数组分为两部分，已排序部分和未排序部分。不断的从未排序部分选取最小值，将其放在已排序部分的末尾。

最大特点是交换移动数据次数相当少。

**选择排序不是稳定排序**。比如：5，8，5，2，9。使用选择排序算法来排序的话，第一次找到最小元素 2，与第一个 5 交换位置，那第一个 5 和中间的 5 顺序就变了，所以就不稳定了。正是因此，相对于冒泡排序和插入排序，选择排序就稍微逊色了。

[代码实现：](src/select_sort.py)
```python
class SelectSort(object):
    def sleect_sort(self, arr):
        arr_size = len(arr)
        for i in range(arr_size):
            min_index = i
            for j in range(i + 1, arr_size):
                if (arr[j] < arr[min_index]):
                    min_index = j
            if (i != min_index):
                arr[i], arr[min_index] = arr[min_index], arr[i]
```

### 三、插入排序

插入排序也是将数组分为两部分，已排序部分和未排序部分。

取未排序部分的第一个元素从已排序部分的尾部开始比较，直到找到插入位置。

代码实现：
```Python
class InsertSort(ISort):
    
    def sort(self, arr):
        arr_size = len(arr)
        for i in range(1, arr_size):
            temp = arr[i]
            current_index = i
            while current_index > 0 and arr[current_index - 1] > temp:
                arr[current_index] = arr[current_index - 1]
                current_index -= 1
            if current_index != i:
                arr[current_index] = temp
```

#### 四、归并排序
> 将长度为n的记录不断划分，划分到长度为1时，再两两合并，依次递归。主要是利用分治法来处理。

代码实现：

```
@Override
public int[] sort(int[] arr) {
    mergeSort(arr, 0, arr.length - 1);
    return arr;
}
private void mergeSort(int[] array, int start, int end) {
    if (start >= end) return;
    int middle = (start + end) / 2;
    mergeSort(array, start, middle);
    mergeSort(array, middle + 1, end);
    merge(array, start, middle, end);
}
private void merge(int[] array, int start, int middle, int end) {
    int[] aux = new int[end - start + 1];
    System.arraycopy(array, start, aux, 0, end - start + 1);
    int left = start;
    int right = middle + 1;
    for (int k = start; k <= end; k++) {
        if (left > middle) {
            array[k] = aux[right - start];
            right++;
        } else if (right > end) {
            array[k] = aux[left - start];
            left++;
        } else if (aux[left - start] > aux[right - start]) {
            array[k] = aux[right - start];
            right++;
        } else {
            array[k] = aux[left - start];
            left++;
        }
    }
}
```

#### 五、堆排序
> 堆排序就是利用堆进行排序的方法.基本思想是:将待排序的序列构造成一个大顶堆.此时,整个序列的最大值就是堆顶的根结点.将它移
走(其实就是将其与堆数组的末尾元素交换, 此时末尾元素就是最大值),然后将剩余的n-1个序列重新构造成一个堆,这样就会得到n个元
素的次大值.如此反复执行,便能得到一个有序序列了。

步骤：

1. 构造最大堆（Build_Max_Heap）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。

2. 堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。

3. 最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点 。

代码实现：

```
public int[] sort(int[] arr) {
    int len = arr.length - 1;
    for (int i = len / 2 - 1; i >= 0; i--) {
        headAdjust(arr, i, len);
    }
    while (len >= 0) {
        SortUtil.swap(arr, 0, len--);
        headAdjust(arr, 0, len);
    }
    return arr;
}
private void headAdjust(int[] arr, int parent, int len) {
    int leftChild, rightChild, maxChild;
    while ((leftChild = 2 * parent + 1) <= len) {
        rightChild = leftChild + 1;
        maxChild = leftChild;
        // 将maxChild指向左右子节点中的较大者
        if (maxChild < len && (arr[leftChild] < arr[rightChild])) {
            maxChild++;
        }
        if (arr[parent] < arr[maxChild]) {
            SortUtil.swap(arr, parent, maxChild);
            parent = maxChild;
        } else {
            break;
        }
    }
}
```

#### 六、希尔排序
> 先将整个待排元素序列分割成若干子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，然后依次缩减增量再进行排
序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序（增量为1）。其时间复杂度为O(n^3/2),要好于直接
插入排序的O(n^2)

代码实现:

```
int gap = arr.length / 2;
while (gap >= 1) {
    for (int i = gap; i < arr.length; i++) {
        int temp = arr[i];
        int j = i - gap;
        while (j >= 0 && arr[j] > temp) {
            arr[j + gap] = arr[j];
            j -= gap;
        }
        arr[j + gap] = temp;
    }
    gap /= 2;
}
```

注：希尔排序的gap取值不仅仅是arr.length/2这么简单，可以根据数据特性选取合适的值达到最高的运行效率。

#### 七、快速排序
> 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤：

1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。

代码实现：

```
private void quickSort(int[] arr, int left, int right) {
    if (left >= right) return;
    int i = left, j = right, temp = arr[left];
    while (i < j) {
        while (i < j && arr[j] >= temp) {
            j--;
        }
        while (i < j && arr[i] <= temp) {
            i++;
        }
        if (i < j) {
            SortUtil.swap(arr, i, j);
        }
    }
    arr[left] = arr[i];
    arr[i] = temp;
    quickSort(arr, left, i - 1);
    quickSort(arr, i + 1, right);
}
```