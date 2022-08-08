def mergeArr(arr, s, e):
    
    mid = (s + e)//2
    
    len1 = mid - s + 1
    len2 = e - mid

    arr1 = [None] * len1
    arr2 = [None] * len2
    
    # copy values
    mainArrayIndex = s
    for i in range(0, len1):
        arr1[i] = arr[mainArrayIndex]
        mainArrayIndex += 1
        
    mainArrayIndex = mid + 1
    for i in range(0, len2):
        arr2[i] = arr[mainArrayIndex]
        mainArrayIndex += 1
        
    # merge 2 sorted array
    index1 = 0
    index2 = 0
    mainArrayIndex = s
    
    while (index1<len1 and index2<len2):
        if arr1[index1] < arr2[index2]:
            arr[mainArrayIndex] = arr1[index1]
            mainArrayIndex += 1
            index1 += 1
        else:
            arr[mainArrayIndex] = arr2[index2]
            mainArrayIndex += 1
            index2 += 1
    
    while (index1<len1):
        arr[mainArrayIndex] = arr1[index1]
        mainArrayIndex += 1
        index1 += 1
        
    while (index2 < len2):
        arr[mainArrayIndex] = arr2[index2]
        mainArrayIndex += 1
        index2 += 1
    return arr
            
def mergeSort(arr, s, e):
    
    # Base Case
    if s >= e:
        return
    
    mid = (s + e)//2
   
    # left part sort karna hai
    mergeSort(arr, s, mid)
  
    # Right sort karna hai
    mergeSort(arr, mid+1, e)
    
    # merge
    return mergeArr(arr, s, e)
    
arr = [38,27,43,3,9,82,10]
s = 0
e = len(arr)-1
print(mergeSort(arr, s, e))