### 前文

O(n^2)的算法
   - 冒泡排序
   - 选择排序
   - 插入排序
  
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

### 四、归并排序
归并排序使用的思想是分治思想，将一个大问题分解成小问题来解决。

归并排序的核心思想：如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起，这样整个数组就都有序了。

[代码实现：](src/merge_sort.py)
```python
class MergeSort(ISort):
    
    def sort(self, arr):
        left = 0
        right = len(arr) - 1
        self.mergeSort(arr, left, right)
    
    # 将数组从中间分为两部分，然后合并
    def mergeSort(self, arr, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    # 合并两个数组，合并时要注意排序
    def merge(self, arr, left, mid, right):
        mergeNum = []
        start = left
        end = mid + 1
        while start <= mid and end <= right:
            if arr[start] <= arr[end]:
                mergeNum.append(arr[start])
                start += 1
            else:
                mergeNum.append(arr[end])
                end += 1
        
        while start <= mid:
            mergeNum.append(arr[start])
            start += 1
        while end <= right:
            mergeNum.append(arr[end])
            end += 1
        
        # 将辅助数组的数据拷贝回原数组
        start = left
        while start <= right:
            arr[start] = mergeNum[start - left]
            start += 1
```

### 五、堆排序
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

### 六、快速排序
#### 1.快排原理及实现
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤：

1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。

[代码实现:](src/quick_sort.py)

```python
class QuickSort(ISort):
    
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 默认取第一个元素为基准
        point = arr[left]
        while left < right:
            while right > left and arr[right] >= point:
                right -= 1
            arr[right], arr[left] = arr[left], arr[right]

            while right > left and arr[left] <= point:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        return left
```

#### 2.优化：减少交换次数

上面的实现里，每次left和right变动都要做两次交换，而每次交换其实都是基准值与left或者right定位到的值进行的交换，因此可以优化这里的交换次数。

[代码实现:](src/quick_sort.py)
```python
# 优化：减少元素交换。  
class QuickSort1(ISort):

    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 默认取第一个元素为基准(注意这里记录的是基准的索引)
        point = left
        while left < right:
            while right > left and arr[right] >= arr[point]:
                right -= 1

            while right > left and arr[left] <= arr[point]:
                left += 1
            
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        # 此时left=right，并且是基准值的合适位置，将基准值赋予arr[left]
        arr[left], arr[point] = arr[point], arr[left]
        return left
```

#### 3.优化：随机基准值

**在待排序列是部分有序时，固定选取枢轴使快排效率底下，要缓解这种情况，就引入了随机选取枢轴**。
思路：使用随机数生成函数生成一个随机数randInt，随机数的范围为[left, right]，将这个基准值与left交换，然后按照以上的排序进行操作即可。

优点：这是一种相对安全的策略。由于枢轴的位置是随机的，那么产生的分割也不会总是会出现劣质的分割。在整个数组数字全相等时，仍然是最坏情况，时间复杂度是O(n^2）。实际上，随机化快速排序得到理论最坏情况的可能性仅为1/(2^n）。所以随机化快速排序可以对于绝大多数输入数据达到O(nlogn）的期望时间复杂度。

[代码实现:](src/quick_sort.py)
```python
import random

# 优化：随机选取基准值。 
class QuickSort2(ISort):

    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 随机选取基准值
        randInt = random.randint(left, right)
        # 将选取的基准值与left交换
        arr[left], arr[randInt] = arr[randInt], arr[left]
        # 交换完后，基准值还是left
        point = left
        while left < right:
            while right > left and arr[right] >= arr[point]:
                right -= 1

            while right > left and arr[left] <= arr[point]:
                left += 1
            
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        # 此时left=right，并且是基准值的合适位置，将基准值赋予arr[left]
        arr[left], arr[point] = arr[point], arr[left]
        return left
```