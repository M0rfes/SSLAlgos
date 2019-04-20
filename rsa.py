import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
plainl_text = input("Enter your text \n")
key_us = int(input("Enter an integer"))
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)  # generate pub and priv key

publickey = key.publickey()  # pub key export for exchange
msg = [ord(char) for char in plainl_text]
encrypted = [key.encrypt(pt, key_us) for pt in msg]
# message to encrypt is in the above line 'encrypt this message'

for ctext in encrypted:
    print(ctext, '\n')  # ciphertext


decrypted = [chr(key.decrypt(ast.literal_eval(str(ct)))) for ct in encrypted]

print('decrypted:', "".join(decrypted))
