# Find the Union and Intersection of the two sorted arrays.

def union(arr1,arr2):
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    arr3 = []
    while (i < m) and (j < n):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        
        elif arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
        
        elif arr1[i] == arr2[j]:
            arr3.append(arr1[i])
            i += 1
            j += 1
    
    # printing remaining elements of larger array

    while (i < m):
        arr3.append(arr1[i])
        i += 1

    while (j < n):
        arr3.append(arr2[j])
        j += 1

    return len(arr3)


print(union(arr1=[1,2,3,4,5], arr2=[1,2,3]))
    