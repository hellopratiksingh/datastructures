def isSorted(arr, n):
    if n == 0 or n == 1:
        return True
    
    if arr[0] > arr[1]:
        return False
    
    else:
        return isSorted(arr[1:], n-1)
    
    # Base Case:
    # if there is only one element in the list. it will considered as sorted
    # if the current element is greater than next then it is not sorted.
    
    # RR
    # after checking first element we will call function passing 
    # remaining arr and length (n - 1)
