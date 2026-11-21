from pycipher import SimpleSubstitution

# key = "MQWERTYUIOPASDFGHJKLZXCVBN"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
cipher = SimpleSubstitution(key)

encrypted = cipher.encipher("HELLO WORLD")
encrypted_alpha = cipher.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
decrypted = cipher.decipher(encrypted)
decrypted_alpha = cipher.decipher(encrypted_alpha)


print(encrypted)
# print(encrypted_alpha)
print(decrypted)
# print(decrypted_alpha)