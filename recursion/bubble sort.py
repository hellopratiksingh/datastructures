def bubble(arr, n):
    if n == 0 or n==1:
        return arr
    
    
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
    return bubble(arr, n-1)


arr = [2,5,1,6,9]        
print(bubble(arr, 5))