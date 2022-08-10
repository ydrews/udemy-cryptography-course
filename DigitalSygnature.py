import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


# this are Alice's RSA keys
# Public Key(e, n): 11 131773
# Secret Key(d) 3971
n = 131773
e = 5
d = 3971


# This is the message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

# Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h_alice = int.from_bytes(h, "big") % n
print("Hash value", h)
# Step 2: decrypt the hash value (use secret exponent)
sign = h_alice**d % n
# Step 3: send message with signature to Bob
print(message, sign)


# This is Eve being evil and modifies the message
# INSERT CODE HERE THAT MODIFIES THE MESSAGE
# message = modify(message)


# Bob verifying the signature
# Step 1: calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h_bob = int.from_bytes(h, "big") % n
print("Hash value", h_bob)
# Step 2: Verify the signature
verification = sign**e % n
print("Verification value", verification)
if verification != h_bob:
    print("Message has been modified")
else:
    print("Verification correct")
