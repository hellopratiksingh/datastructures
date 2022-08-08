# Print first n bonachi numbers:
# n is subarray , m is total number of elements

def nbonachi(n, m):
    # first n numbers
    arr = [0] * (n - 1)
    arr.append(1)
    sum_ = 0
    start = 0
    #
    for i in range(n, m):
        for j in range(start, i):
            sum_ += arr[j]
        arr.append(sum_)
        start += 1
        sum_ = 0

    return arr


print(nbonachi(4, 10))
