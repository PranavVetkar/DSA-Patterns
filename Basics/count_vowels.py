def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    s.strip()
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = "Hello World"
print(count_vowels(input_string))