def count_occurrence(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count = count + 1
    return count

arr = [1, 2, 3, 4, 5, 3, 3]
target = 3
print(count_occurrence(arr, target))