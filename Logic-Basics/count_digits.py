def count_digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count

print(count_digits(12345))