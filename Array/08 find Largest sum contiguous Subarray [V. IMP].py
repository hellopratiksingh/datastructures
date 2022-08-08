# find Largest sum contiguous Subarray [V. IMP]
# 1
def maxsum(arr, k, n):
    max = 0
    for i in range(0, n-k+1):
        z=i
        j=0
        sum=0
        while j < k:
            sum +=arr[z]
            z+=1
            j+=1

        
        if sum >  max:
            max =sum

    return max    


# 2
def maxk(arr, k, n):
    z=0
    sum=0
    for i in range(0,n):
        z+=1
        sum+=arr[i]
        if(z%k==0):
            if(sum>max):
                max=sum
            z=0
            sum=0
    return max

