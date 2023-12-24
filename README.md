# RSA-
The code implements an RSA encryption and decryption system along with a client-server communication setup.

Key generation includes functions to generate random prime numbers, calculate the greatest common divisor, and find the multiplicative inverse modulo.

Encryption and decryption functions utilize the RSA algorithm to secure messages.

RSA key pairs are generated with a default size of 2048 bits.

The client and server communicate over the local network (127.0.0.1) on different ports (12346 for the server and 12345 for the client).

The server generates an RSA key pair, sends the public key to the client, and receives an encrypted message.

The client receives the public key, encrypts a user-input message, and sends the encrypted message to the server.

The server decrypts the received message and prints the result.

The RSA key size can be adjusted by changing the parameter in generate_rsa_keypair(bits).

The server and client scripts are meant to be run separately, and the server must be running before the client connects.
