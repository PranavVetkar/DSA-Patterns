def find_peak_element(arr):
    n = len(arr)
    if n == 0:
        return None
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
            return arr[i]
    return None

arr = [1, 3, 20, 4, 1, 0]
print(find_peak_element(arr))