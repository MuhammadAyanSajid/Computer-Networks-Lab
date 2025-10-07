import socket
import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 1234)

print("Type your message :\n")
print("exit to quit\n")

while True:
    message = input("Msg: ")
   
    time_send = datetime.datetime.now()

    client_socket.sendto(message.encode(), server_address)

    if message.lower() == "exit":
        print("Terminating connection...")
        break

    data, server = client_socket.recvfrom(1024)
    time_receive = datetime.datetime.now()

    rtt = (time_receive - time_send).total_seconds() * 1000  

    print("Server:", data.decode())
    print(f"RTT: {rtt:} ms\n")

client_socket.close()
print("Client closed successfully.")