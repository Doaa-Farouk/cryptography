# p is the alphabetical order
# k is the key

# 1- Encryption
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
        
# print(affine('CYBER',21,5))  # This should result in VPALY
print(affine('doaa',21,9))  # This should result in VPALY
print(affine('DOAA',21,9))  # This should result in URJJ


# 2- Find the inverse : mm is the inverse for m relvent to 26
def inverse(m,relevant):
    for i in range(100):
        mm = (relevant* i + 1)
        if mm % m == 0:
            return mm/m
    
print(inverse(21,26)) # This should result in 5

# 3- Decryption
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
        
print(decrypt_affine('VPALY',5,5))  # This should result in CYBER