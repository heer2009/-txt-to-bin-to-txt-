def binary_to_text(binary_string):
    # Remove any spaces or extra characters
    binary_string = binary_string.replace(' ', '')
    
    # Ensure the length of binary_string is a multiple of 8
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length should be a multiple of 8.")
    
    # Split the binary string into chunks of 8 bits
    n = 8
    chunks = [binary_string[i:i+n] for i in range(0, len(binary_string), n)]
    
    # Convert each binary chunk to a character
    text = ''.join(chr(int(chunk, 2)) for chunk in chunks)
    
    return text

# Example usage
binary_input = "01001000 01100101 01101100 01101100 01101111"
text_output = binary_to_text(binary_input)
print(text_output)  #output should be in text
