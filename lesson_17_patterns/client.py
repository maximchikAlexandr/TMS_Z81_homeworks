import socket

from interface import SocketInterface

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SocketInterface.address)
MESSAGE_IN = ""

while MESSAGE_IN != "0":
    message_out = client_socket.recv(2048).decode("utf-8")
    if message_out.startswith("info:"):
        print(f"\nShop:\n{message_out[5:]}\n")
    else:
        print(f"\nShop:\n{message_out}\n")
        MESSAGE_IN = input("Customer: ")
        client_socket.send(MESSAGE_IN.encode("utf-8"))

client_socket.close()
