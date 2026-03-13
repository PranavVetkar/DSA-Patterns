def reverse_integer(num):
    if num < 0:
        return 0
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    if reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

print(reverse_integer(123))