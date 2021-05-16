from ISort import ISort

class BubbleSort(ISort):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if (arr[j] > arr[j + 1]):
                    # swap arr[j] and arr[j + 1]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    

    # 冒泡排序的优化。当某一次冒泡操作没有发生交换时，说明数据都有序了。
    # 这种情况可以提前退出。
    def sort1(self, arr):
        n = len(arr)
        for i in range(n):
            isSwap = False
            for j in range(n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSwap = True
            if not isSwap:
                break
