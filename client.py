import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    msg = input("Enter message: ")
    if msg.lower() == "exit":
        break
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024).decode()
    print("Received from server:", data)

client_socket.close()