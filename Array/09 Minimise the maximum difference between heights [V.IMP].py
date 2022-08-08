# Minimise the maximum difference between heights [V.IMP]
# Assume that height of the tower can be negative

def getMinDiff(arr, n, k):
    # code here
    arr.sort()
    max_ = arr[n-1]
    min_ = arr[0]
    res_ = max_ - min_

    for i in range(1, n):
        max_ = max(arr[i-1]+k, arr[n-1]-k)
        min_ = min(arr[i]-k, arr[0]+k)

        res_ = min(res_, max_ - min_)

    return res_


print(getMinDiff(arr=[2, 6, 3, 4, 7, 2, 10, 3, 2, 1], n=10, k=5))
