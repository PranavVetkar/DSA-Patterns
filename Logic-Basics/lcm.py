def lcm(a, b):
    max_num = max(a, b)
    if max_num % a == 0 and max_num % b == 0:
        return max_num
    else:
        for i in range(max_num, a * b + 1, max_num):
            if i % a == 0 and i % b == 0:
                return i

print(lcm(4, 6))