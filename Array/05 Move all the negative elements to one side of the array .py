# Move all the negative elements to one side of the array

def negative_elements(arr):
    n =len(arr)
    low, hi = 0, n-1
    while (low <= hi):
        if (arr[low] < 0) and (arr[hi] > 0):
            low += 1
            hi -= 1
        
        elif (arr[low] > 0) and (arr[hi] < 0):
            arr[low], arr[hi] = arr[hi], arr[low]
            low += 1
            hi -= 1

        elif (arr[low] < 0) and (arr[hi] < 0):
            low += 1

        elif (arr[low] > 0) and (arr[hi] > 0):
            hi -= 1 
        
    return arr

print(negative_elements(arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]))
