def text_to_binary(text):
    # Convert each character to its ASCII value and then to an 8-bit binary string
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

# Example usage
text_input = "Hello"
binary_output = text_to_binary(text_input)
print(binary_output)  # Output should be the binary representation of "Hello"