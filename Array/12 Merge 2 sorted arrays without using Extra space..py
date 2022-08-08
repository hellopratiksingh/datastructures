# Merge 2 sorted arrays without using Extra space.

def merge(arr1, arr2, n, m):
    # code here
    for i in arr1:
        arr2.append(i)
    arr2.sort()
    for i in range(0, n):
        arr1[i] = arr2[i]
    for i in range(0, m):
        arr2[i] = arr2[n+i]
    z = len(arr2)
    del arr2[m:z]

    return arr1,arr2


print(merge(arr1=[1, 3, 5, 7], arr2=[0, 2, 6, 8, 9], n=4, m=5))
