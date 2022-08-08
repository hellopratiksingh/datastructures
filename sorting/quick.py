def pratikSort(arr):
    j = 0
    
    while j < len(arr):
        count = 0
        for i in range(j, len(arr)):
            curr = arr[j]
            if arr[i] < curr:
                count += 1
        arr[j], arr[j+count] = arr[j+count], arr[j]
        j += 1
    return arr

arr = [3,5,1,8,2,4]
print((pratikSort(arr))