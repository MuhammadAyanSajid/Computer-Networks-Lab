import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('localhost', 12345))
print("DateTime UDP Server is running on port 12345...")

print("UDP Server is running and waiting for client request...")
while True:
    data, client_address = server_socket.recvfrom(1024)
    
    print("Request from:", client_address)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_socket.sendto(time.encode(), client_address)