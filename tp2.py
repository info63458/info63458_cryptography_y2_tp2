#start
from math import *

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0 :
            return False
    return True


print(isPrime(9))
print(isPrime(7))

# def RSA_encryption(p,q,m):

