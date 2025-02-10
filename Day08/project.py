def encode(message, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""
    for char in message:
        if char in letters:
            index = (letters.index(char) + shift) % 26
            encoded_message += letters[index]
        else:
            encoded_message += char
    return encoded_message

def decode(message, shift):
    return encode(message, -shift)

def advance_decode(message):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for shift in range(1, 26):
        decoded_message = ""
        for char in message:
            if char in letters:
                index = (letters.index(char) - shift) % 26
                decoded_message += letters[index]
            else:
                decoded_message += char
        print(f"Decoded message: {decoded_message} with shift = {shift}")

def main():
    while True:
        print('''
1. Encode
2. Decode
3. Advance Decode
4. Exit
''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            message = input("Enter the message you want to encode: ").lower()
            shift = int(input("Enter the shift you want in your encoded message: "))
            print(f"Your encoded message is: {encode(message, shift)}")
        elif choice == 2:
            message = input("Enter the message you want to decode: ").lower()
            shift = int(input("Enter the shift you want in your decoded message: "))
            print(f"Your decoded message is: {decode(message, shift)}")
        elif choice == 3:
            message = input("Enter the message you want to advance decode: ").lower()
            advance_decode(message)
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid input")
