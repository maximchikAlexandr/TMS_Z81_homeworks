"""
Класс SocketInterface создает функции ввода-вывода для обмена сообщениями между клиентом и сервером

Класс TerminalInterface создает функции ввода-вывода в терминал. Для имитации обмена сообщениями
между клиентом и сервером

Класс InterfaceFactory созадет экземпляр класса SocketInterface или TerminalInterface в зависимости
от выбранного типа интерфейса
"""

import socket


class SocketInterface:
    address = ('127.0.0.1', 55237)
    ENCODING = 'utf-8'

    def __init__(self):
        self.socket = socket.create_server(self.address, family=socket.AF_INET)
        print('server started\nwaiting for client to accept connection')
        self.client_sock, self.client_addr = self.socket.accept()
        print(f'accept connection: {self.client_addr}')

    def create_io_funcs(self):
        def input_from_user(prompt_string):
            self.client_sock.send(prompt_string.encode(self.ENCODING))
            data = self.client_sock.recv(1024)
            return data.decode(self.ENCODING)

        def print_to_user(message):
            message = f"info:{message}"
            self.client_sock.send(message.encode(self.ENCODING))

        return input_from_user, print_to_user

    def close(self):
        self.socket.close()


class TerminalInterface:

    def create_io_funcs(self):
        return self.add_name(input), self.add_name(print)

    @staticmethod
    def add_name(func):
        def inner(prompt_string):
            print("\nShop:")
            if func.__name__ == "input":
                prompt_string += "\nCustomer: "
            res = func(prompt_string)
            return res

        return inner

    def close(self):
        pass


class InterfaceFactory:
    interfaces = {
        "socket": SocketInterface,
        "terminal": TerminalInterface,
    }

    @classmethod
    def create_interface(cls, type_interface):
        if type_interface in cls.interfaces:
            return cls.interfaces[type_interface]()
