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
2
def decrypt(message, shift):
    return encrypt(message, -shift)

def main():

    while True:

        print("\n===== Caesar Cipher =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")

        if choice == "3":
            print("Thank you for using Caesar Cipher!")
            break

        message = input("Enter input message: ")

        while True:
            try:
                shift = int(input("Enter  value to shift by: "))
                break
            except ValueError:
                print(" Please enter a correct number.")

        if choice == "1":
            print("Encrypted:", encrypt(message, shift))

        elif choice == "2":
            print("Decrypted:", decrypt(message, shift))

        else:
            print(" Incorrect Choice")

if __name__ == "__main__":
    main()