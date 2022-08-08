# Prefix Sum
def prefix_sum(arr):
    ps = []
    ps.append(arr[0])
    curr_sum = arr[0]
    
    for i in range(1, len(arr)):
        curr_sum += arr[i]
        ps.append(curr_sum)

    return ps

# Get sum (start, end)

def getSum(l, r, ps):
    if l == 0:
        return ps[r]
    else:
        return ps[r] - ps[l-1]


res = (prefix_sum(arr=[2,8,3,9,6,5,4]))
print(getSum(l=0, r=2, ps=res))
print(getSum(l=1, r=3, ps=res))
print(getSum(l=2, r=6, ps=res))
