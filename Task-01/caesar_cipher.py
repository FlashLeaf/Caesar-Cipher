def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

# User input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
else:
    result_text = caesar_cipher(message, shift_value, mode)
    print(f"Result: {result_text}")
