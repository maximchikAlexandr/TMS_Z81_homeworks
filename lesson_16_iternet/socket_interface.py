"""
класс SocketInterface:
- возвращает объект socket для сервера или клиента
- создает функции ввода-вывода для обмена сообщениями между клиентом и сервером
"""

import socket


class SocketInterface:
    address = ('127.0.0.1', 55237)
    ENCODING = 'utf-8'

    def __init__(self, create_server=True):
        self.socket = self.__get_server_socket() if create_server else self.__get_client_socket()

    def get_socket(self):
        return self.socket

    def __get_server_socket(self):
        return socket.create_server(self.address, family=socket.AF_INET)

    def __get_client_socket(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(self.address)
        return client_socket

    def create_network_io_funcs(self, client_socket):
        def network_input(prompt_string):
            client_socket.send(prompt_string.encode(self.ENCODING))
            data = client_socket.recv(1024)
            return data.decode(self.ENCODING)

        def network_print(message):
            message = f"info:{message}"
            client_socket.send(message.encode(self.ENCODING))

        return network_input, network_print
