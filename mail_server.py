import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("SMTP Mail Server is running on port 12345...")

while True:
    connection, address = server_socket.accept()
    print("Connected to:", address)
    
    connection.send(b"220 Mail Server Ready\r\n")
    
    data = connection.recv(1024).decode()
    print("Received:", data)
    connection.send(b"250 Hello\r\n")
    
    data = connection.recv(1024).decode()
    print("Received:", data)
    connection.send(b"250 OK\r\n")
    
    data = connection.recv(1024).decode()
    print("Received:", data)
    connection.send(b"250 OK\r\n")
    
    data = connection.recv(1024).decode()
    print("Received:", data)
    connection.send(b"354 Start mail input\r\n")
    
    data = connection.recv(1024).decode()
    print("Email content:", data)
    connection.send(b"250 Message accepted\r\n")
    
    data = connection.recv(1024).decode()
    print("Received:", data)
    connection.send(b"221 Bye\r\n")
    
    connection.close()
    print("Email received")