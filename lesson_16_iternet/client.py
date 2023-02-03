from socket_interface import SocketInterface

socket_interface = SocketInterface(create_server=False)
client_sock = socket_interface.get_socket()
message_in = ""

while message_in != '0':
    message_out = client_sock.recv(2048).decode('utf-8')
    if message_out.startswith('info:'):
        print(f"\nShop:\n{message_out[5:]}\n")
    else:
        print(f"\nShop:\n{message_out}\n")
        message_in = input("Customer: ")
        client_sock.send(message_in.encode('utf-8'))

client_sock.close()
