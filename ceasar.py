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


def decrypt(pt, key):
    return ceasar(pt, key)


def encrypt(ct, key):
    if key > 0:
        key = -key
    return ceasar(ct, key)


ptext = input('Enter the text to encrypt\n')
key = int(input('Enter the key\n'))
ctext = encrypt(ptext, key)
print(ctext)
print(decrypt(ctext, key))
