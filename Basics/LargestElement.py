def LargestElement(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [3, 1, 4, 1, 5, 9]
print(LargestElement(arr))