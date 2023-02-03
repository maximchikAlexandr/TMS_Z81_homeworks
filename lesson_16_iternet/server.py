from time import sleep

from db.connection import ConnectionDB
from db.table_objects import Customer, Order, OrderData, Product
from socket_interface import SocketInterface

STR_FOR_INPUT = '''Введите:
1 - для регистрации
2 - для заказа товара
3 - для получения информации о конкретном продукте
4 - для получения информации о всех своих заказах
5 - для получения информации о всех продуктах с определенной скидкой
6 - для предрасчета заказа
0 - выход'''

socket_interface = SocketInterface()
serv_sock = socket_interface.get_socket()
print('server started')

client_sock, client_addr = serv_sock.accept()
network_input, network_print = socket_interface.create_network_io_funcs(client_sock)
print(f'accept connection: {client_addr}')

conn_db = ConnectionDB()
cursor = conn_db.cursor()

try:
    while True:
        input_var = int(network_input(STR_FOR_INPUT))
        if input_var == 1:
            new_customer = Customer(network_input('Введите ваше имя'),
                                    int(network_input('Введите ваш возраст')),
                                    network_input('Введите ваш адрес'),
                                    int(network_input('Сумма пополнения баланса')),
                                    cursor=cursor)
            new_customer.add_new_customer()
            conn_db.commit()
            network_print("Пользователь успешно добалавлен!\n")

        elif input_var == 2:
            customer_name = network_input('Введите имя покупателя:')
            product_name = network_input('Введите наименование товара:')
            product_count = int(network_input('Введите количество товара:'))
            product = Product(product_name, cursor)
            if product_count > product.get_count_to_stock():
                network_print('Вы не можете заказать товара больше, чем есть на складе!')
                continue
            Order.add_new_order(product_count, customer_name, product_name, cursor)
            product.write_off_product(product_count)
            conn_db.commit()
            product_data = product.get_product_data()
            order_data = OrderData(product_name, product_data.price,
                                   product_data.discount, product_count)
            network_print(str(order_data))

        elif input_var == 3:
            product_name = network_input('Введите наименование товара:')
            product = Product(product_name, cursor)
            product_data = product.get_product_data()
            network_print(str(product_data))

        elif input_var == 4:
            customer_name = network_input('Введите имя покупателя:')
            orders = Order.get_orders_by_customer_name(customer_name, cursor)
            message = ""
            for num, order in enumerate(orders, start=1):
                message += f"\nЗаказ №{num}\n{str(order)}"
            network_print(message)

        elif input_var == 5:
            discount = int(network_input('Введите размер скидки в %:'))
            products = Product.get_products_by_discount(discount, cursor)
            message = ""
            for num, product_data in enumerate(products, start=1):
                message += f"\nТовар №{num}\n{str(product_data)}"
            network_print(message)

        elif input_var == 6:
            product_name = network_input('Введите наименование товара:')
            product_count = int(network_input('Введите количество товара:'))
            product = Product(product_name, cursor)
            if product_count > product.get_count_to_stock():
                network_print('Вы не можете заказать товара больше, чем есть на складе!')
                continue
            product_data = product.get_product_data()
            order_data = OrderData(product_name, product_data.price,
                                   product_data.discount, product_count)
            network_print(str(order_data))
        sleep(0.3)

except (BrokenPipeError, ConnectionResetError, ValueError) as err:
    print("Соединение прервано")
    print(err)
finally:
    serv_sock.close()
    cursor.close()
    cursor = None
    conn_db.close()
