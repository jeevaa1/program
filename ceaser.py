def caesar_cipher(message, key, mode):
    # Create an empty string to store the encrypted/decrypted message
    result = ""

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to its ASCII code
            code = ord(char.upper())

            # Apply the key value to the ASCII code, depending on the mode
            if mode == "encrypt":
                code = (code - 65 + key) % 26 + 65
            elif mode == "decrypt":
                code = (code - 65 - key) % 26 + 65

            # Convert the ASCII code back to a character and add it to the result string
            result += chr(code)
        else:
            # If the character is not a letter, add it to the result string unchanged
            result += char

    return result

# Get the user input for the message, key, and mode
message = input("Enter the message: ")
key = int(input("Enter the key value: "))
mode = input("Enter 'encrypt' or 'decrypt': ")

# Encrypt or decrypt the message using the Caesar cipher
if mode == "encrypt":
    encrypted_message = caesar_cipher(message, key, mode)
    print("Encrypted message:", encrypted_message)
elif mode == "decrypt":
    decrypted_message = caesar_cipher(message, key, mode)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid mode entered. Please enter 'encrypt' or 'decrypt'.")
