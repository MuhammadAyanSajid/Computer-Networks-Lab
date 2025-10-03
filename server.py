import socket

# 1. Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Echo Server listening on port 12345...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        echo_message = "Echo: " + message
        conn.sendall(echo_message.encode())
    conn.close()
    print(f"Connection with {addr} closed.")