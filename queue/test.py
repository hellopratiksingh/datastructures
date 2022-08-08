def search(nums, target):
    s, e = 0, len(nums) - 1
    while s < e:
        mid = (s + e) // 2
        if nums[mid] >= nums[0]:
            s = mid + 1
        else:
            e = mid

    if nums[s] <= target and target <= nums[len(nums)-1]:
        s = s
        e = len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return -1

    else:
        s = 0
        e = s - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return -1

    return

print(search(nums=[1,3], target=1))