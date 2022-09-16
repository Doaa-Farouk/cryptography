# encryption

def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
            
    return("" . join(key))

def vigenere(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i])) % 26
        if chr(x) == ' ':
            encrypt_text.append(chr(x))
            continue
        x += ord('A')
        encrypt_text.append(chr(x))
    return("" . join(encrypt_text))

def caeser_cipher(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
            continue
        if (char.isupper()):
            result += chr((ord(char) - 65 + s) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + s) % 26 + 97)   
    return result

# mix vigenere and caeser cipher

plain_text= input('Enter word you want to encrypt: ')
first_key= input('Enter key to decrypt: ')
generated_key= generate_key(plain_text,first_key)
v_text= vigenere(plain_text,generated_key)
c_text= caeser_cipher(v_text,len(generated_key))
print(f'Your word is: {plain_text}')
print(f'Your encrypted word is: {c_text}')

# decryption

def decrypt_caeser(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
            continue
        if (char.isupper()):
            result += chr((ord(char)- 65 - s ) % 26 + 65)
            
        else:
            result += chr((ord(char)- 97 - s ) % 26 + 97)
    return result

def decrypt_vigenere(encrypt_text, key):
    orig_text = []
    
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) -ord(key[i])) % 26
        if chr(x) == ' ':
            orig_text.append(chr(x))
            continue
        x += ord('A')
        orig_text.append(chr(x))
        
    return("" . join(orig_text))

        
c_decrypted_text= decrypt_caeser(c_text,len(generated_key))
print(f'The decrypetd word from caeser is:{c_decrypted_text}')
v_decrypted_text= decrypt_vigenere(c_decrypted_text,generated_key)
print(f'The decrypted word is:{v_decrypted_text}')