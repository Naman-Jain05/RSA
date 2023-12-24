

import random
import math
import sympy

def generate_prime(bits):
    p = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    q = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    return p,q
    

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext

# Function to decrypt a ciphertext with the private key
def decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    phi_copy = phi

    while e > 0:
        q = phi_copy // e
        phi_copy, e = e, phi_copy % e
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1

    if phi_copy == 1:
        d = y2 + phi
        if d < 0:
            d += phi
        return d

def generate_rsa_keypair(bits):
    
    p,q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Common choice for the public exponent

    if gcd(e, phi) == 1:
        d = multiplicative_inverse(e, phi)
        return ((n, e), (n, d),(p,q))
    else:
        return generate_rsa_keypair(bits)

# Generate an RSA key pair (2048 bits)
public_key, private_key, primes = generate_rsa_keypair(2048)

# Extract the RSA components
n, e = public_key
n, d = private_key
p,q = primes

# # Print the RSA components
# print("Modulus (n):", n)
# print("Public Exponent (e):", e)
# print("Private Exponent (d):", d)
# print("Prime Factor 1 (p):", p)
# print("Prime Factor 2 (q):", q)
# plaintext = 12
# ciphertext = encrypt(public_key,plaintext)
# decryptedtext = decrypt(private_key,ciphertext)

# print("Plaint Text : ",plaintext)
# print("Ciphertext : ",ciphertext)
# print("Decrypted Text : ",decryptedtext)


