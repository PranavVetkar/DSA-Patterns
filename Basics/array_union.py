def array_union(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.union(set2))

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(array_union(arr1, arr2))