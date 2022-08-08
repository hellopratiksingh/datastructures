def solve(nums, ans, index):
    # base case
    if index >= len(nums):
        ans.append(nums.copy())
        return

    for j in range(index, len(nums)):
        nums[index], nums[j] = nums[j], nums[index]
        # recursion
        solve(nums, ans, index+1)
        # backtrack
        nums[index], nums[j] = nums[j], nums[index]

def nextPermutation(nums):
    ans = []
    index = 0
    solve(nums, ans, index)
    return ans
    
print(nextPermutation([1,2,3]))