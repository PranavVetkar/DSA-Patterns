def SecondLargest(arr):
    arr.sort()
    if len(arr) >= 2:
        return arr[-2]
    return None

arr = [3, 1, 4, 1, 5, 9]
print(SecondLargest(arr))