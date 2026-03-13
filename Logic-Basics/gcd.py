def gcd(x, y):
    if y == 0:
        return x
    else:
        max = x if x > y else y
        min = y if x > y else x
        for i in range(min, 0, -1):
            if max % i == 0 and min % i == 0:
                return i
            
print(gcd(48, 18))