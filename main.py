def encrypt(message, shift):
    encrypted = ""

    for char in message:

        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            encrypted += char

    return encrypted

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    print("===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Choose (1/2): ")

    message = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    if choice == "1":
        result = encrypt(message, shift)
        print("Encrypted:", result)

    elif choice == "2":
        result = decrypt(message, shift)
        print("Decrypted:", result)

    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()