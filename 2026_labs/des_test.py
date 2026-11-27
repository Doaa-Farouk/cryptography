from Crypto.Cipher import DES

key = bytes.fromhex("133457799BBCDFF1")
block = bytes.fromhex("0123456789ABCDEF")

print(DES.new(key, DES.MODE_ECB).encrypt(block).hex())

# print(dir(DES))

print(len("133457799BBCDFF1"))
print(16*8)

cipher = DES.new(key)
ct = cipher.encrypt(block)
print(cipher.decrypt(ct).hex()) 



