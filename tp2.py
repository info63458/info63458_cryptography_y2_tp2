#start
from math import *

def isPrime(n):
    n=int(input())
    for i in range(math.sqrt(n)):
        if n%i == 0 :
            return False
        else :
            return True
    print(isPrime)

# def RSA_encryption(p,q,m):

