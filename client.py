import socket
import pickle
from RSA import encrypt

def client():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12346))

    # Receive the public key from the server
    public_key = client_socket.recv(1024)
    public_key = pickle.loads(public_key)

    # Encrypt a message using the public key
    mssg=int(input("Enter your integer:"))
    plaintext = mssg
    ciphertext = encrypt(public_key, plaintext)

    # Send the encrypted message to the server
    client_socket.send(pickle.dumps(ciphertext))

    client_socket.close()

if __name__ == "__main__":
    client()
