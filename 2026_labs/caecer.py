from pycipher import Caesar

cipher = Caesar(2)

encrypted = cipher.encipher("ABCD")
print(encrypted)  # KHOOR

decrypted = cipher.decipher(encrypted)
print(decrypted)  # HELLO