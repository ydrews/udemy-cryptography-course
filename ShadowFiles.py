import hashlib
import base64

iterations = 45454
salt = base64.b64decode(
    "6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
# SALTED-SHA512-PBKDF2

password = "password".encode()
# Insert code here
v = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
value = base64.b64encode(v)


# --------
iterations = 45454
salt_alice = "test".encode()
password_alice = "password".encode()
value_alice = base64.b64encode(hashlib.pbkdf2_hmac(
    "sha512", password_alice, salt_alice, iterations, dklen=128))
print(value_alice, salt_alice, iterations)

salt_bob = "test2".encode()
password_bob = "password".encode()
value_bob = base64.b64encode(hashlib.pbkdf2_hmac(
    "sha512", password_bob, salt_bob, iterations, dklen=128))
print(value_bob, salt_bob, iterations)
