import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 32
    return bytes(l)

# Alice and Bob has secret key
secret_key = "secret_key".encode()

# Alice wants to compute HMAC
m = "Bob you are still awesome".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print("Message:", m)
print("HMAC:", hmac)

# Eve comes along
m = modify(m)
print("Modified:", m)

# Bob receives and validates HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print("Message:", m)
print("HMAC:", hmac)
