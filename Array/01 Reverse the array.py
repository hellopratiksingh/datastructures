# Find the maximum and minimum element in an array

def reverse(arr):
    n = len(arr)
    start, end = 0, n-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print(reverse(arr=[3,4,5,2,7,8]))
