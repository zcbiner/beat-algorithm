class SelectSort(object):
    def sort(self, arr):
        arr_size = len(arr)
        for i in range(arr_size):
            min_index = i
            for j in range(i + 1, arr_size):
                if (arr[j] < arr[min_index]):
                    min_index = j
            if (i != min_index):
                arr[i], arr[min_index] = arr[min_index], arr[i]
