def mergeSort(arr, left, right):
    def merge(arr, left, mid, right):    
        arr1 = []
        arr2 = []
        res = []
        
        while left < mid:
            arr1.append(arr[left])
            left += 1
            
        while mid < right:
            arr2.append(arr[mid])
            mid += 1            
            
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            
            else:
                res.append(arr2[j])
                j += 1
            
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        
 
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
    
                
        return arr
              
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        res = merge(arr, left, mid, right)
        return res
print(mergeSort([15,20,30,5,25,80], 0, 6))