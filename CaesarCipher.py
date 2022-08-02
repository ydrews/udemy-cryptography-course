def generate_key(n):
    letters = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decryption_key(key):
    d_key = {}
    for c in key:
        d_key[key[c]] = c
    return d_key


key = generate_key(3)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)

# try to break it
print(cipher)
for i in range(26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)
