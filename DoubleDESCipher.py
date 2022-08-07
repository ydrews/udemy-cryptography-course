from pyDes import *
import random

message = "01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_12 = random.randrange(0, 256)
key_2 = bytes([key_12, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0]*8)


k_1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k_2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

print(message)
cipher = k_1.encrypt(k_2.encrypt(message))
print("Key 11: ", key_11)
print("Key 12: ", key_12)
print("encrypted:", cipher)

message = k_2.decrypt(k_1.decrypt(cipher))
print("decrypted:", message)


# attack
lookup = {}

for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i


for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("key 11: ", i)
        print("key 12: ", lookup[k.decrypt(cipher)])
        key_1 = bytes([i, 0, 0, 0, 0, 0, 0, 0])
        key_2 = bytes([lookup[k.decrypt(cipher)], 0, 0, 0, 0, 0, 0, 0])
        k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
        k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)
        print("Eve breaking double DES: ", k2.decrypt(k1.decrypt(cipher)))
        break
