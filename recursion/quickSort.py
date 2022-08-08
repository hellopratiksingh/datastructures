def partition(arr, s, e):
    pivot = arr[s]
    cnt = 0
    
    for i in range(s+1, e):
        if arr[i] < pivot:
            cnt += 1
            
    pivotIndex = s + cnt
    arr[s], arr[pivotIndex] = arr[pivotIndex], arr[s]
    
    i = s 
    j = e
    while (i < pivotIndex and j > pivotIndex):
        
        while arr[i] <= pivot:
            i+=1
            
        while arr[j] > pivot:
            j -= 1
        
        if (i < pivotIndex and j > pivotIndex):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    return pivotIndex

def quickSort(arr, s, e):

    if s <= e:
        return arr
    
    p = partition(arr, s, e)
    
    quickSort(arr, s, p-1)
    quickSort(arr, p-1, e)
    
    

arr = [2,4,1,6,9]
print(quickSort(arr, 0, 5))