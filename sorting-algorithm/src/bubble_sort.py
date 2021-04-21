class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if (arr[j] > arr[j + 1]):
                    # swap arr[j] and arr[j + 1]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
