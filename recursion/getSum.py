def getSum(arr, n, sum=0):
    if n == 0:
        return 0
    
    if n == 1:
        return arr[0]
    
    else:
        return arr[0] + getSum(arr[1:], n-1)
        

arr = [3]
print(getSum(arr, n=1))
