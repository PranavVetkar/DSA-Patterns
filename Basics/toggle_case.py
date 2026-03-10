def toggle_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

# Example usage:
input_string = "Hello World!"
print(toggle_case(input_string))