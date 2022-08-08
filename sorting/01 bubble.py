def bubble(arr):
    n = len(arr)
    for j in range(1, n):
        for i in range(0, n-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubble([64, 34, 25, 12, 22, 11, 90]))
