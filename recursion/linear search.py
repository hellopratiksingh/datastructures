def linearSearch(arr, n, k):
    if n == 0:
        return "Not Found"
    
    if arr[0] == k:
        return "Found"
    
    else:
        return linearSearch(arr[1:], n-1, k)
        

arr = [1,2,3,4,5]

print(linearSearch(arr, 5, 3))