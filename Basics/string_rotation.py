def check_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    temp = str1 + str1
    return temp.find(str2) != -1

# Example usage:
str1 = "abcde"
str2 = "deabc"
print(check_rotation(str1, str2))  # Output: True