# find duplicate in an array of N+1 Integers

def findDuplicate(nums):
    n = len(nums)
    temp = [0] * n
    for i in nums:
        if temp[i] == 0:
            temp[i] = 1
        else:
            return i
        
        

print(findDuplicate(nums=[3,1,2,4,2]))
