class InsertSort(object):
    def insert_sort(self, arr):
        arr_size = len(arr)
        for i in range(1, arr_size):
            temp = arr[i]
            current_index = i
            while current_index > 0 and arr[current_index - 1] > temp:
                arr[current_index] = arr[current_index - 1]
                current_index -= 1
            if current_index != i:
                arr[current_index] = temp

if __name__ == '__main__':
    arr = [2, 67, 23, 34, 0, 11, 66, 8, 3, 12]
    InsertSort().insert_sort(arr)
    for i in range(len(arr)):
        print("%d" %arr[i]),