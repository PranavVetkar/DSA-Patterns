def array_intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))

arr1 = [1, 2, 2, 3]
arr2 = [2, 3, 4]
print(array_intersection(arr1, arr2))