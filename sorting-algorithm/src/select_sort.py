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

if __name__ == '__main__':
    arr = [2, 67, 23, 34, 0, 11, 66, 8, 3, 12]
    SelectSort().sleect_sort(arr)
    for i in range(len(arr)):
        print("%d" %arr[i]),
