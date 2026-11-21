# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for letter in "GYBNQKURP":
#     print(alpha.index(letter))
# print("=" *20)
# for letter in "ACT":
#     print(alpha.index(letter))    

from pycipher import HillCipher
hc = HillCipher("beaf")
print(hc.encrypt("Love Python"))
print(hc.decrypt("PITTOO"))


6 24 1
13 16 10
20 17 15
POHRNA