def subarray_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    prefix_sum_freq = {0: 1}
    for num in arr:
        prefix_sum += num
        if (prefix_sum - k) in prefix_sum_freq:
            count += prefix_sum_freq[prefix_sum - k]
        if prefix_sum in prefix_sum_freq:
            prefix_sum_freq[prefix_sum] += 1
        else:
            prefix_sum_freq[prefix_sum] = 1
    return count

arr = [1, 1, 1]
k = 2
print(subarray_sum_k(arr, k))