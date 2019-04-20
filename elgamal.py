
import Crypto.Util.number as num
import random


def pair(s):
    safe_prime = 0
    while(True):
        p = num.getPrime(s)
        safe_prime = 2*p+1
        if(num.isPrime(safe_prime)):
            break
    while(True):
        a = random.randint(2, safe_prime-1)
        if((safe_prime-1) % a != 1):
            break

    return safe_prime, a


def egKey(s):
    p, a = pair(s)
    x = random.randint(1, p-2)
    y = pow(a, x, p)
    return p, a, x, y


""" Signature Generation 
"""


def egGen(p, a, x, m):
    while 1:
        k = random.randint(1, p-2)
        if num.GCD(k, p-1) == 1:
            break
    r = pow(a, k, p)
    l = num.inverse(k, p-1)
    s = l*(m-x*r) % (p-1)
    return r, s


""" Signature Verification 
"""


def egVer(p, a,	y, r, s, m):
    if r < 1 or r > p-1:
        return False
    v1 = pow(y, r, p) % p * pow(r, s, p) % p
    v2 = pow(a, m, p)
    return v1 == v2

#####################################################################
# Tests


if __name__ == "__main__":

    message = 36
    print("Message: ", message)
    prime, alpha, private, public = egKey(10)
    print("prime,alpha,private,public", prime, alpha, private, public)
    rr, ss = egGen(prime, alpha, private, message)
    print("rr,ss", rr, ss)
    isValid = egVer(prime, alpha, public, rr, ss, 37)
    print("Valid Signature: ",  isValid)
