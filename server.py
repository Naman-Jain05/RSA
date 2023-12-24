import socket
import pickle
from RSA import generate_rsa_keypair, encrypt, decrypt

def serve():
    # Generate RSA key pair
    public_key, private_key, primes = generate_rsa_keypair(1024)

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12346))
    server_socket.listen(1)

    print("Server is listening...")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send the public key to the client
    client_socket.send(pickle.dumps(public_key))

    # Receive encrypted message from the client
    ciphertext = client_socket.recv(1024)
    ciphertext = pickle.loads(ciphertext)

    # Decrypt the message
    decrypted_text = decrypt(private_key, ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    serve()
