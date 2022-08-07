from pyDes import *


def modify(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ 2
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

message = "Give Bob:    10$"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)


cipher = k.encrypt(message)
# Alice sending the encrypted message
# encrypt the message to cipher
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))

# Bob decrypting the cipher text
cipher = modify(cipher)

# decrypt the cipher to message
message = k.decrypt(cipher)
print("Decrypted:", message)
