import socket
client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'', ('localhost', 12345))
date, addr = client.recvfrom(1024)
date = date.decode()

print("Current Date & Time from Server:", date)

client.close()