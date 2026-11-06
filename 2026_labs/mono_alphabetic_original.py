import string

# alphabet = string.ascii_uppercase
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
key = "QWERTYUIOPASDFGHJKLZXCVBNM0987123456"
# print(alphabet)

def encrypt(text):
    result = ""

    for char in text.upper():
        if char in alphabet:
            index = alphabet.index(char)
            # The .index() method returns the position of the character in the string.
            result += key[index]
            # This gets the character from the key at the same position and adds it to result.
        else:
            # The .index() method returns the position of the character in the string.
            result += char

    return result

def decrypt(text):
    result = ""

    for char in text.upper():
        if char in key:
            index = key.index(char)
            result += alphabet[index]
        else:
            result += char

    return result


# message = "HELLO WORLD"
message = input("Write a message to encrypt:")

encrypted = encrypt(message)
# decrypted = decrypt(encrypted)

# print("Original:", message)
print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)



