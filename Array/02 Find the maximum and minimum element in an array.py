# Find the maximum and minimum element in an array

def max_element(arr):
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i

    return (max, min)


print(max_element(arr=[3, 4, 5, 2, 7, 8]))
