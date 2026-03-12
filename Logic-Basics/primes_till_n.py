def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def prime_till_n(num):
    if num < 2:
        print("No primes")
        return
    while num >= 2:
        if prime(num):
            print(num)
        num = num-1

prime_till_n(50)