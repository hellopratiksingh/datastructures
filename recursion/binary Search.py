def binarySearch(arr, s, e, k):
    if s > e:
        return False
    
    mid = (s + e)//2
    
    if arr[mid] == k:
        return True
    
    if arr[mid] < k:
        return binarySearch(arr, mid+1, e, k)
    
    else:
        return binarySearch(arr, s, mid-1, k)
    

arr = [2,4,6,10,14,18]
print(binarySearch(arr, 0, 5, 24))
    