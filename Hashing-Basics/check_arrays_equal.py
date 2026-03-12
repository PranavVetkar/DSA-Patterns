def check_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    frequency_map = {}
    for num in arr1:
        if num not in frequency_map:
            frequency_map[num] = 1
        else:
            frequency_map[num] += 1
    for num in arr2:
        if num not in frequency_map or frequency_map[num] == 0:
            return False
        frequency_map[num] -= 1
    return True

arr1 = [1, 2, 3, 4]
arr2 = [4, 3, 2, 1]
print(check_arrays_equal(arr1, arr2))