from time import sleep

from db.connection import ConnectionDB
from db.table_objects import Customer, Order, OrderData, Product
from interface import InterfaceFactory

STR_FOR_INPUT = """Нажмите:
любую клавишу - для запуска сервера
1 - для запуска в терминале
Ваш выбор: """

TYPE_INTERFACE = "terminal" if input(STR_FOR_INPUT) == "1" else "socket"
interface = InterfaceFactory.create_interface(TYPE_INTERFACE)
input_from_user, print_to_user = interface.create_io_funcs()

conn_db = ConnectionDB()
cursor = conn_db.cursor()

STR_FOR_INPUT = '''Введите:
1 - для регистрации
2 - для заказа товара
3 - для получения информации о конкретном продукте
4 - для получения информации о всех своих заказах
5 - для получения информации о всех продуктах с определенной скидкой
6 - для предрасчета заказа
0 - выход'''
INPUT_VAR = 10

try:
    while INPUT_VAR != 0:
        INPUT_VAR = int(input_from_user(STR_FOR_INPUT))
        if INPUT_VAR == 1:
            new_customer = Customer(input_from_user('Введите ваше имя'),
                                    int(input_from_user('Введите ваш возраст')),
                                    input_from_user('Введите ваш адрес'),
                                    int(input_from_user('Сумма пополнения баланса')),
                                    cursor=cursor)
            new_customer.add_new_customer()
            conn_db.commit()
            print_to_user("Пользователь успешно добалавлен!\n")

        elif INPUT_VAR == 2:
            customer_name = input_from_user('Введите имя покупателя:')
            product_name = input_from_user('Введите наименование товара:')
            product_count = int(input_from_user('Введите количество товара:'))
            product = Product(product_name, cursor)
            if product_count > product.get_count_to_stock():
                print_to_user('Вы не можете заказать товара больше, чем есть на складе!')
                continue
            Order.add_new_order(product_count, customer_name, product_name, cursor)
            product.write_off_product(product_count)
            conn_db.commit()
            product_data = product.get_product_data()
            order_data = OrderData(product_name, product_data.price,
                                   product_data.discount, product_count)
            print_to_user(str(order_data))

        elif INPUT_VAR == 3:
            product_name = input_from_user('Введите наименование товара:')
            product = Product(product_name, cursor)
            product_data = product.get_product_data()
            print_to_user(str(product_data))

        elif INPUT_VAR == 4:
            customer_name = input_from_user('Введите имя покупателя:')
            orders = Order.get_orders_by_customer_name(customer_name, cursor)
            message = ""
            for num, order in enumerate(orders, start=1):
                message += f"\nЗаказ №{num}\n{str(order)}"
            print_to_user(message)

        elif INPUT_VAR == 5:
            discount = int(input_from_user('Введите размер скидки в %:'))
            products = Product.get_products_by_discount(discount, cursor)
            message = ""
            for num, product_data in enumerate(products, start=1):
                message += f"\nТовар №{num}\n{str(product_data)}"
            print_to_user(message)

        elif INPUT_VAR == 6:
            product_name = input_from_user('Введите наименование товара:')
            product_count = int(input_from_user('Введите количество товара:'))
            product = Product(product_name, cursor)
            if product_count > product.get_count_to_stock():
                print_to_user('Вы не можете заказать товара больше, чем есть на складе!')
                continue
            product_data = product.get_product_data()
            order_data = OrderData(product_name, product_data.price,
                                   product_data.discount, product_count)
            print_to_user(str(order_data))
        sleep(0.3)

except (BrokenPipeError, ConnectionResetError, ValueError) as err:
    print("Соединение прервано")
    print(err)
finally:
    interface.close()
    cursor.close()
    cursor = None
    conn_db.close()
