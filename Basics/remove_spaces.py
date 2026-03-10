
def remove_spaces(s):
    result = ""
    
    for char in s:
        if char != ' ':
            result += char
            
    return result

input_string = "  Hello World  "
print(remove_spaces(input_string))