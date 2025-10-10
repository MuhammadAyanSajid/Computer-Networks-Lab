import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 1234))
print("Server running on port 1234")

os.makedirs("received_files", exist_ok=True)

while True:
    data, client_address = server_socket.recvfrom(4096)
    message = data.decode()
    
    if message == "ping":
        server_socket.sendto("pong".encode(), client_address)
    elif message.startswith("FILE:"):
        filename, filesize = message.split(":")[1:3]
        server_socket.sendto("READY".encode(), client_address)  
        
        file_data = b""
        while len(file_data) < int(filesize):
            chunk = server_socket.recvfrom(4096)[0]
            file_data += chunk
            server_socket.sendto("ACK".encode(), client_address)  
        
        with open(f"received_files/{filename}", "wb") as f:
            f.write(file_data)
        server_socket.sendto("File received".encode(), client_address)
    elif message == "exit":
        break

server_socket.close()