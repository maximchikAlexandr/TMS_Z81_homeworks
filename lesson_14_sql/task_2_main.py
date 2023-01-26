from my_connection import get_connection
from task_2_table_objects import Customer, Order, OrderData, Product

STR_FOR_INPUT = '''
Введите:
1 - для регистрации
2 - для заказа товара
3 - для получения информации о конкретном продукте
4 - для получения информации о всех своих заказах
5 - для получения информации о всех продуктах с определенной скидкой
6 - для предрасчета заказа
0 - выход

Ваш ответ: '''

input_var = 1

with get_connection('tms') as conn:
    with conn.cursor() as cursor:
        try:

            while input_var != 0:
                input_var = int(input(STR_FOR_INPUT))

                if input_var == 1:
                    new_customer = Customer(input('Введите ваше имя:\n'),
                                            int(input('Введите ваш возраст:\n')),
                                            input('Введите ваш адрес:\n'),
                                            int(input('Сумма, на которую пополняете баланс:\n')),
                                            cursor=cursor)
                    new_customer.add_new_customer()
                    print("Пользователь успешно добалавлен!")

                elif input_var == 2:
                    customer_name = input('Введите имя покупателя:\n')
                    product_name = input('Введите наименование товара:\n')
                    product_count = int(input('Введите количество товара:\n'))
                    product = Product(product_name, cursor)
                    if product_count > product.get_count_to_stock():
                        print('Вы не можете заказать товара больше, чем есть на складе!')
                        continue
                    Order.add_new_order(product_count, customer_name, product_name, cursor)
                    product.write_off_product(product_count)
                    conn.commit()
                    product_data = product.get_product_data()
                    order_data = OrderData(product_name, product_data.price,
                                           product_data.discount, product_count)
                    order_data.pretty_print()

                elif input_var == 3:
                    product_name = input('Введите наименование товара:\n')
                    product = Product(product_name, cursor)
                    product_data = product.get_product_data()
                    product_data.pretty_print()

                elif input_var == 4:
                    customer_name = input('Введите имя покупателя:\n')
                    orders = Order.get_orders_by_customer_name(customer_name, cursor)
                    for num, order in enumerate(orders, start=1):
                        print(f"Заказ №{num}")
                        order.pretty_print()

                elif input_var == 5:
                    discount = int(input('Введите размер скидки в %:\n'))
                    products = Product.get_products_by_discount(discount, cursor)
                    for num, product_data in enumerate(products, start=1):
                        print(f'Товар № {num}')
                        product_data.pretty_print()

                elif input_var == 6:
                    product_name = input('Введите наименование товара:\n')
                    product_count = int(input('Введите количество товара:\n'))
                    product = Product(product_name, cursor)
                    if product_count > product.get_count_to_stock():
                        print('Вы не можете заказать товара больше, чем есть на складе!')
                        continue
                    product_data = product.get_product_data()
                    order_data = OrderData(product_name, product_data.price,
                                           product_data.discount, product_count)
                    order_data.pretty_print()

        except ValueError:
            raise ValueError("Вводить только целые числа!")
