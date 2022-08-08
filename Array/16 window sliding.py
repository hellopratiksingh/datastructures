# k = Size of window

def window_sliding(arr, k):
    curr_sum = 0
    for i in range(0, k):
        curr_sum += arr[i]

    max_sum = curr_sum

    for j in range(k, len(arr)):
        curr_sum = ((curr_sum - arr[j-k]) + arr[j])
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


print(window_sliding(arr=[1, 8, 30, -5, 20, 7], k=3))
