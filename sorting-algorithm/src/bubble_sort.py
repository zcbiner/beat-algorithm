class BubbleSort:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if (arr[j] > arr[j + 1]):
                    # swap arr[j] and arr[j + 1]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [2, 67, 23, 34, 0, 11, 66, 8, 3, 12]
    BubbleSort().bubble_sort(arr)
    for i in range(len(arr)):
        print("%d" %arr[i]),