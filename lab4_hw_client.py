import socket
import datetime
import os
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)
server_address = ('localhost', 1234)

start_time = datetime.datetime.now()
client_socket.sendto("ping".encode(), server_address)
data, client_address = client_socket.recvfrom(1024)
rtt = (datetime.datetime.now() - start_time).total_seconds() * 1000
print(f"RTT: {rtt:.2f} ms")

if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
    filename = os.path.basename(sys.argv[1])
    filesize = os.path.getsize(sys.argv[1])
    
    client_socket.sendto(f"FILE:{filename}:{filesize}".encode(), server_address)
    client_socket.recvfrom(1024) 

    with open(sys.argv[1], "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            client_socket.sendto(chunk, server_address)
            client_socket.recvfrom(1024)  # Wait for ACK
    
    print(client_socket.recvfrom(1024)[0].decode())

client_socket.sendto("exit".encode(), server_address)
client_socket.close()