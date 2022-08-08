# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort012(arr, n):
    low, mid, hi = 0, 0, n-1
    while (mid < hi):
        if (arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        if (arr[mid] == 1):
            mid += 1

        if (arr[mid] == 2):
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr


print(sort012(arr=[2,1,2,0], n=4))
