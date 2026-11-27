letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(message, key):
    encrypted_text = ""

    for letter in message.upper():
            letter_index = letters.index(letter) 
            new_letter = key[letter_index]
            encrypted_text += new_letter

    return encrypted_text

print(encrypt("ABCDHelloWorld","QWERTYUIOPASDFGHJKLZXCVBNM"))
