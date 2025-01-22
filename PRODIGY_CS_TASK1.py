def caesar_cipher_tool(message, key, operation='encrypt'):
    transformed_text = ''
    for character in message:
        if character.isalpha():
            base = 65 if character.isupper() else 97
            new_position = (ord(character) - base + (key if operation == 'encrypt' else -key)) % 26
            transformed_text += chr(new_position + base)
        else:
            transformed_text += character
    return transformed_text

while True:
    print("\n=== Welcome to the Caesar Cipher Program ===")
    print("1. Encrypt a text")
    print("2. Decrypt a text")
    print("3. Exit the program")
    user_choice = input("Select an option (1, 2, or 3): ")

    if user_choice == '3':
        print("Thank you for using the Caesar Cipher Program. Goodbye!")
        break
    elif user_choice in ('1', '2'):
        action = 'encrypt' if user_choice == '1' else 'decrypt'
        user_message = input("Type your text here: ")
        shift_value = int(input("Enter the shift amount: "))
        output = caesar_cipher_tool(user_message, shift_value, action)
        print(f"The {action}ed result is: {output}")
    else:
        print("Oops! That option is not valid. Please try again.")
