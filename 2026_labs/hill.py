import string 
import numpy as np
from math import gcd 

# class HillCipher:
#     key_string = string.ascii_uppercase
#     modules = np.vectorize(lambda x: x %26 )
#     to_int = np.vectorize(round)



arr = np.array([[6, 24 ,1], [13, 16 ,10], [20, 17 ,15]])
# print(arr)
# print(arr.ndim)

# def test_u(x):
#     return x % 26
    
# result = np.vectorize(test_u)
# print(result(arr))

det = round(np.linalg.det(arr))
print(det)

# 6 24 1
# 13 16 10
# 20 17 15
