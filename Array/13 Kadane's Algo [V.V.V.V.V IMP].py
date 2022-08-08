# Kadane's Algo [V.V.V.V.V IMP]

def maxSubArraySum(arr, N):
    ##Your code here
    max_ = 0
    curr_ = 0
    umax = max(arr)
    for i in range(0, N):
        curr_ = curr_ + arr[i]

        if curr_ > max_:
            max_ = curr_

        if curr_ < 0:
            curr_ = 0

        if umax < 0:
            return umax

    return max_


print(maxSubArraySum(arr=[1, 2, 3, -2, 5], N=5))
