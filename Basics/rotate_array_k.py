def rotate_array_k(nums, k):
    k = k % len(nums) 
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array_k(arr, k))