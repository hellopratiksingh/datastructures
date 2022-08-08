def majorityElement(nums):
    hashmap = {}
    for i, n in enumerate(nums):
        if n not in hashmap:
            hashmap[n] = 1
        else:
            hashmap[n] += 1
    for num in hashmap:
        if hashmap[num] > len(nums)/2:
            return num
    return -1
            
            
print(majorityElement([2,1,1,1,2,2,1]))