def frequency_map(arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    return freq_map

arr = [1, 2, 2, 3, 3, 3]
print(frequency_map(arr))