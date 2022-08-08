# given an array of n elements with given sum 
# return sub array of any size 

def window_sliding2(arr, sum):
    curr_sum = 0
    sub_arr = []
    i = 0
    while curr_sum <= sum:
        curr_sum += arr[i]
        sub_arr.append(arr[i])
        i += 1

    if curr_sum == sum:
        return sub_arr
    else:
        i = 0
        while curr_sum > sum:
            curr_sum = curr_sum - arr[i]
            sub_arr.remove(arr[i])
            i += 1
    return sub_arr


print(window_sliding2(arr=[1, 4, 20, 3, 10], sum=30))
