def find_minimum(arr):
    if len(arr) == 0:
        return None
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

arr = [5, 2, 9, 1, 5, 6]
print(find_minimum(arr))