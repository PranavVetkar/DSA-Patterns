def single_number(nums):
    seen = []
    for item in nums:
        if item not in seen:
            seen.append(item)
        else:
            seen.remove(item)
    return seen

arr = [2, 2, 1, 3, 3]
print(single_number(arr))