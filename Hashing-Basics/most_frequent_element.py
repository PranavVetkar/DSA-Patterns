def most_frequent_element(nums):
    frequency = {}
    max_freq = 0
    most_freq_element = None
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_freq:
            max_freq = frequency[num]
            most_freq_element = num
    return most_freq_element

nums = [1, 2, 3, 2, 4, 1, 2]
print(most_frequent_element(nums))