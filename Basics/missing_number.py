def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

arr = [0, 1, 2, 4, 5]
print(missing_number(arr))