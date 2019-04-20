import string
import collections


def ceasar(msg, key):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    upper.rotate(key)
    lower.rotate(key)
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    return msg.translate(upper.maketrans(string.ascii_uppercase, upper)).translate(lower.maketrans(string.ascii_lowercase, lower))


def encrypt(pt, key):
    return ceasar(pt, key)


def decrypt(ct, key):
    if key > 0:
        key = -key
    return ceasar(ct, key)


ptext = input('Enter the text to encrypt')
key = int(input('Enter the key'))
ctext = encrypt(ptext, key)
print(ctext)
print(decrypt(ctext, key))
