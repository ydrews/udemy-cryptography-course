import random


def xor(x, s):
    print(bin(x), 'xor', bin(s), '=', bin(x ^ s))


def generate_key_stream(n):
    return bytes([random.randrange(0, 250) for i in range(n)])


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


# this is done by the enemy
msg = "DO ATTACK"
message = msg.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)


# this is us trying to break it
print(cipher)
msg = "NO ATTACK"
message = msg.encode()
guess_key_string = xor_bytes(message, cipher)
print(xor_bytes(guess_key_string, cipher))
