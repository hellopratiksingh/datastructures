def insertion(arr):
    n = len(arr)
    for i in range(0, n-1):
        minIndex = i
        # finding min index
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        #inserting min number at left
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


print(insertion([64, 34, 25, 12, 22, 11, 90]))
