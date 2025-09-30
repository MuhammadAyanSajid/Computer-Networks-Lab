import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))
msg = input("Enter message: ")
client_socket.send(msg.encode())
data = client_socket.recv(1024).decode()
print( data)

client_socket.close()
