def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for letters in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
             if letters >= value:
                 result += letter
                 letters -= value
             else:
                result += '-'

    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------