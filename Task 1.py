# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char  
    return encrypted_text

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift) 

# Main program
def caesar_cipher():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (or 'Q' to quit): ").upper()
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please choose 'E', 'D', or 'Q'.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
