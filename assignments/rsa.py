# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are relatively small compared to practical application

import math
def gcd(p, g):
    temp = 0
    while(1):
        temp = p % g
        if (temp == 0):
            return g
        p = g
        g = temp
        
p = int(input('Enter p :'))
g = int(input('Enter g :'))
n = p * g
phi = (p-1)*(g-1)
e = 11
# e must be co-prime(relative primes) to phi and smaller than phi.
while (e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
print(f'this is e: {e}')
# Private key (d stands for decrypt) 
# choosing d such that it satisfies d*e = 1 + k * totient

r = 1
while(True):
    if (math.fmod((1 + (phi* r)),e) == 0.0):
        break
    else:
        r = r+ 1
        
d = (1 + (phi* r))/e

# Message to be encrypted
msg = int(input('Enter m :'))
print("Message data = ", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e )
c = math.fmod(c, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
# This code is contributed by Pranay Arora


# Output :
# Message data = 12.000000
# Encrypted data = 3.000000
# Original Message Sent = 12.000000