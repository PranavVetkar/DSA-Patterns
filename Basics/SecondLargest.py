def SecondLargest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

arr = [3, 1, 4, 1, 5, 9]
print(SecondLargest(arr))