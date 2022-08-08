def binary(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + ((end-start) // 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else: 
            end = mid - 1
    return -1

print(binary([2,5,6,7,8,10,12,13], 15))
                
        
        
    