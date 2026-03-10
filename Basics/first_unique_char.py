def first_unique_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None

input_string = "leetcode"
print(first_unique_char(input_string))