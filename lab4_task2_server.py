import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('localhost', 1234))
print("UDP Echo Server is running on port 1234...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Received from {client_address}: {message}")

    if message.lower() == "exit":
        print("Client requested termination. Shutting down server...")
        break

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reply = f"Echo: {message} | Server Time: {current_time}"
    server_socket.sendto(reply.encode(), client_address)

server_socket.close()
print("Server closed successfully.")