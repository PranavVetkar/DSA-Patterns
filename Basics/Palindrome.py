def Palindrome(s):
    if s == s[::-1]:
        return True
    return False

s = "Madam"
print(Palindrome(s))

s = "Hello"
print(Palindrome(s))