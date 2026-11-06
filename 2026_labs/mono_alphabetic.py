from pycipher import SimpleSubstitution

key = "MQWERTYUIOPASDFGHJKLZXCVBN"
cipher = SimpleSubstitution(key)

encrypted = cipher.encipher("AHELLO WORLD")
decrypted = cipher.decipher(encrypted)

print(encrypted)
print(decrypted)