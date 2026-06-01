#start
from math import *

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0 :
            return False
    return True


#print(isPrime(9))
#print(isPrime(7))

def RSA_encryption(p,q,m):
    # STOP USING INPUT GODDAMNIT
    if isPrime(p) and isPrime(q) :
        print("The numbers are prime")
    else : 
        print("Please choose prime numbers")
    return #returns None but it isn't printed, unnecessary as it doesn't return a value

RSA_encryption(9,7,11)