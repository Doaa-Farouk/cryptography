def caesar_cipher(text, key):
    result = ""

    for char in text.upper():
        if char.isalpha() and char.isascii():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char

    return result

print(caesar_cipher("HELLO", 3))   # KHOOR
print(caesar_cipher("KHOOR", -3))  # HELLO