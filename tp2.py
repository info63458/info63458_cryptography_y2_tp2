#start
from math import *

def isPrime(y):
    for i in range(2,int(sqrt(y))+1):
        if y%i == 0 :
            return False
    return True

def GCD(a, b): #Returns the GCD of a and b (Euclidean algorithm).
    while b != 0:
        a, b = b, a % b #swap
    return abs(a) #return absolute value of a
#taken from the TP pdf

print(GCD(84,126)) #test works

def RSA_encryption(p,q,m):
    # STOP USING INPUT GODDAMNIT
    if isPrime(p) and isPrime(q) :
        print("The numbers are prime")
        n=p*q
        phi=(p-1)*(q-1)
    else : 
        print("Please choose prime numbers")
    return #returns None but it isn't printed, unnecessary as it doesn't return a value

RSA_encryption(23,29,8)