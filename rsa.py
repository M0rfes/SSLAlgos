from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
plainl_text = input("Enter your text \n")
plainl_text = bytes(plainl_text, 'utf-8')
num1 = int(input("Enter one Prime Number"))
num2 = int(input("Enter another Prime Number"))


def gen_key(num1, num2):
    random_generator = Random.new(num1, num2).read
    key = RSA.generate(1024, random_generator)  # generate pub and privat key
    f = open('mykey.pem', 'wb')
    f.write(key.export_key('PEM'))
    f.close()
    return key


def encrypt(pText, num1, num2):
    publickey = gen_key(num1, num2).publickey()  # pub key export for exchange
    encryptor = PKCS1_OAEP.new(publickey)
    cyText = encryptor.encrypt(plainl_text)
    return cyText


def decrypt(cyText):
    f = open('mykey.pem', 'r')
    key = RSA.import_key(f.read())
    f.close()
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(cyText)))
    return decrypted


cipher = encrypt(plainl_text, num1, num2)
print("Encrypted text:\n", cipher)
decrypted = decrypt(cipher)
print("Decrypted Text:\t", decrypted)
