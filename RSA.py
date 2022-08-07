import math
import random


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


def lcm(a, b):
    return a*b//math.gcd(a, b)  # integer division //


def get_e(l):
    for e in range(2, l):
        if math.gcd(e, l) == 1:
            return e
    return False


def get_d(e, l):
    for d in range(2, l):
        if (d*e) % l == 1:
            return d


def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p

# https://en.wikipedia.org/wiki/RSA_(cryptosystem)

# Key generation done by Alice
# Step 1: generate to distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)

print("Generated primes p and q:", p, q)

# Step 2: compute n = p*q
n = p*q

print("Modulus n:", n)

# Step 3: Compute lambda of n -> λ(n) = lcm(λ(p), λ(q)), λ(p) = p - 1, lcm(a, b) = |ab|/gcd(a, b).
lambda_n = lcm(p - 1, q - 1)
print("Lambda n:", lambda_n)

# Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1;
e = get_e(lambda_n)
print("Public exponent", e)

# Step 5: Determine d as d ≡ e−1 (mod λ(n));
d = get_d(e, lambda_n)
print("Secrete exponent:", d)

# Done with key generation
print("Public Key (e,n):", e, n)
print("Secret Key (d)", d)

# This is Bob wanted to send a message
m = 117
c = (m**e) % n
print("Bob sends c:", c)

# this is Alice decrypting cipher
m = (c**d) % n
print("Alice message:", m)


# this is Eve:
print("Eve sees the following")
print("  Public key:", e, n)
print("  Encrypted cipher", c)

p, q = factor(n)
print("  Factors:", p, q)
lambda_n = lcm(p - 1, q - 1)
print("  Eve: Lambda n:", lambda_n)
d = get_d(e, lambda_n)
print("  Eve: Secrete exponent:", d)
m = (c**d) % n
print("Eve message:", m)


# This is Bob not being careful:
print("This is Bob not being careful")
message = "Alice is awesome"
for m_c in message:
    c = ord(m_c)**e % n
    print(c, " ", end='')
