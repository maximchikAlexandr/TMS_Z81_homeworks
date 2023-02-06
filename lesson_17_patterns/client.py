import socket
from interface import SocketInterface

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SocketInterface.address)
message_in = ""

while message_in != '0':
    message_out = client_socket.recv(2048).decode('utf-8')
    if message_out.startswith('info:'):
        print(f"\nShop:\n{message_out[5:]}\n")
    else:
        print(f"\nShop:\n{message_out}\n")
        message_in = input("Customer: ")
        client_socket.send(message_in.encode('utf-8'))

client_socket.close()
