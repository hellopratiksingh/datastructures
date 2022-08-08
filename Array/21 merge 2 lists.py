def merge(nums1, m, nums2, n):
    
    nums3 = []
    i = 0
    j = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            nums3.append(nums2[j])
            j += 1
        else:
            nums3.append(nums1[i])
            i += 1

    while i < m:
        nums3.append(nums1[i])
        i += 1

    while j < n:
        nums3.append(nums2[j])
        j += 1

    nums1 = nums3
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))