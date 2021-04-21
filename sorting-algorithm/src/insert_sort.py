class InsertSort(object):
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