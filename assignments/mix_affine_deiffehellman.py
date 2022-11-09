def encryption_key(P,G,a,b):
    if __name__ == '__main__':	
        # P = 23
        # G = 9
        
        # a = 4
        # b = 3
        
        x = int(pow(G,a,P))
        y = int(pow(G,b,P))
        
        # Secret key for encryption
        ka = int(pow(y,a,P))
        # print(f'ka= {ka}')
        # Secret key for decryption
        # kb = int(pow(x,b,P))
        return (ka)
        
        
def decryption_key(P,G,a,b):
    if __name__ == '__main__':
        # P = 23
        # G = 9
        # a = 4
        # b = 3
        y = int(pow(G,b,P))
        # print(f'y= {y}')
        x = int(pow(G,a,P))
        # print(f'x= {x}')
        
         # Secret key for encryption
        # ka = int(pow(y,a,P))
        
        # Secret key for decryption
        kb = int(pow(x,b,P))
        return kb



def affine(text, m, k ):
    word = []
    for letter in text:
        if letter == ' ':
            word += letter
            continue
        p = (ord(letter) - 65 ) % 26
        c_num = (m * p + k)% 26
        c = chr(c_num + 65)
        word.append(c)
        
    return ''.join(word)


def decrypt_affine(text, mm, k ):
    word = []
    for letter in text:
        if letter == ' ':
            word += letter
            continue
        c = (ord(letter) - 65 ) % 26
        c_num = (mm * (c - k))% 26
        p = chr(c_num + 65)
        word.append(p)
        
    return ''.join(word)


key= encryption_key(23,9,4,3)
plain_text= input('Enter a word to encrypt:').upper()
ciphered_text= affine(plain_text,21,key)
print(f'ciphered_text is : {ciphered_text}')

d_key= decryption_key(23,9,4,3)
deciphered_text= decrypt_affine(ciphered_text,5,d_key)
print(f'deciphered_text is :{deciphered_text}')