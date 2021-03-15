def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                # swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# The below is test code
arr = [1, 0, 34, 23, 9, 80, 23, 45, 6, 8, 87]
bubbleSort(arr)
for i in range(len(arr)):
    print ("%d" %arr[i]),
