
import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(1)
print("DateTime Server is running on port 12345...")

while True:
   
    connection, address = server_socket.accept()
    print("Connected to:", address)

   
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    connection.send(now.encode())

   
    connection.close()
