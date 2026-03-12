def pair_sum_count(arr, target):
    count = 0
    hash_table = {}
    for num in arr:
        complement = target - num
        if complement in hash_table:
            count += hash_table[complement]
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1
    return count

arr = [1, 2, 3, 4, 3]
target = 6
print(pair_sum_count(arr, target))