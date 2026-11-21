letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(message, key):
    encrypted_text = ""

    for letter in message:
        upper_letter = letter.upper()
        letter_index = letters.index(upper_letter) 
        # print(letter_index)
        new_letter = key[letter_index]
        encrypted_text += new_letter

    return encrypted_text

print(encrypt("HelloWorld","QWERTYUIOPASDFGHJKLZXCVBNM"))