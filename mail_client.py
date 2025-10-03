import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print(client_socket.recv(1024).decode())

sender = input("Enter sender email: ")
recipient = input("Enter recipient email: ")
message = input("Enter message: ")

client_socket.send(b"HELO client\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(f"MAIL FROM:<{sender}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(f"RCPT TO:<{recipient}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(b"DATA\r\n")
print(client_socket.recv(1024).decode())

email = f"From: {sender}\r\nTo: {recipient}\r\n\r\n{message}\r\n.\r\n"
client_socket.send(email.encode())
print(client_socket.recv(1024).decode())

client_socket.send(b"QUIT\r\n")
print(client_socket.recv(1024).decode())

client_socket.close()
print("Email sent")