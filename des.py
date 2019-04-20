from Crypto.Cipher import DES3
from Crypto import Random


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


plaintext = pad(input("Enter your Text\t"))
plaintext = bytes(plaintext, 'utf-8')
key = input("Enter Sisten Bit key\t")
key = bytes(key, 'utf-8')
des = DES3.new(key, DES3.MODE_ECB)
ciphertext = des.encrypt(plaintext)
print("Encrypted Text:\t", ciphertext)
dtext = des.decrypt(ciphertext)
print("Decrypted Text:\t", dtext)
