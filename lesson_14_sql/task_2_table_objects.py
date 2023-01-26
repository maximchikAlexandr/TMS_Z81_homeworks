"""
Классы Customer, Product, Order - для селектов и инсертов в одноименное таблицы в БД
Классы ProductData и OrderData - для хранения информации и красивого вывода в консоль
"""

from dataclasses import dataclass
from typing import List

from psycopg2.extensions import cursor


@dataclass
class Customer:
    name: str
    age: int
    address: str
    balance: int
    cursor: cursor

    def add_new_customer(self) -> None:
        query = """INSERT INTO customers(name, age, address, balance)
                    VALUES (%s, %s, %s, %s)"""
        self.cursor.execute(query, (self.name, self.age, self.address, self.balance))


@dataclass
class ProductData:
    name: str
    price: int
    count: int
    description: str
    discount: int
    category: str

    def pretty_print(self) -> None:
        print(
            f"Наименование: {self.name}\n"
            f"Категория: {self.category}\n"
            f"Стоимость 1 единицы: {self.price}\n"
            f"Скидка: {self.discount} %\n"
            f"Количество на складе: {self.count}\n"
            f"Описание: {self.description}\n\n"
        )


class Product:
    def __init__(self, name: str, cursor_db: cursor) -> None:
        self.name: str = name
        self.cursor: cursor = cursor_db

    def get_product_data(self) -> ProductData:
        query = """SELECT pr.name, pr.price, pr.count_to_stock,
                        pr.description, pr.discount, cat.name
                    FROM products AS pr
                    INNER JOIN category AS cat ON cat.id = pr.category_id
                    WHERE pr.name = %s"""
        self.cursor.execute(query, (self.name,))
        product_fields = self.cursor.fetchone()
        return ProductData(*product_fields)

    def get_count_to_stock(self) -> int:
        query = """SELECT count_to_stock
                    FROM products WHERE name = %s;"""
        self.cursor.execute(query, (self.name,))
        return self.cursor.fetchone()[0]

    def write_off_product(self, count: int) -> None:
        query = """UPDATE products
                    SET count_to_stock = count_to_stock - %s
                    WHERE  name = %s;"""
        self.cursor.execute(query, (count, self.name,), )

    @staticmethod
    def get_products_by_discount(discount: int, cursor_db: cursor) -> List[ProductData]:
        query = """SELECT pr.name, pr.price, pr.count_to_stock,
                        pr.description, pr.discount, cat.name
                    FROM products AS pr
                        INNER JOIN category AS cat ON cat.id = pr.category_id
                    WHERE pr.discount = %s;"""
        cursor_db.execute(query, (discount,))
        products = [ProductData(*item) for item in cursor_db.fetchall()]
        return products

    @staticmethod
    def get_price_with_discount(price: int, discount: int) -> int:
        return int(round(price * (100 - discount) / 100, 0))


@dataclass
class OrderData:
    product_name: str
    product_price: int
    product_discount: int
    product_count: int

    def pretty_print(self) -> None:
        price_with_discount = Product.get_price_with_discount(
            self.product_price, self.product_discount
        )
        print(
            f"Сумма заказа: {self.product_count * price_with_discount} р.\n"
            f"Наименование товара: {self.product_name}\n"
            f"Количество ед. товара: {self.product_count}\n"
            f"Стоимость за ед. товара с учетом скидки: {price_with_discount} р.\n"
        )


class Order:
    @staticmethod
    def add_new_order(product_count: int, customer_name: str,
                      product_name: str, cursor_db: cursor) -> None:
        query = """INSERT INTO orders(product_count, customer_id, product_id)
                    VALUES (%s,
                         (SELECT id FROM customers WHERE name = %s),
                         (SELECT id FROM products WHERE name = %s))"""
        cursor_db.execute(query, (product_count, customer_name, product_name))

    @staticmethod
    def get_orders_by_customer_name(customer_name: str, cursor_db: cursor) -> List[OrderData]:
        query = """SELECT pr.name, pr.price, pr.discount, o.product_count
                    FROM orders AS o
                        INNER JOIN customers AS cus on cus.id = o.customer_id
                        INNER JOIN products AS pr on pr.id = o.product_id
                        INNER JOIN category AS cat on cat.id = pr.category_id
                    WHERE cus.name = %s
                    ORDER BY o.id"""
        cursor_db.execute(query, (customer_name,))
        orders = [OrderData(*item) for item in cursor_db.fetchall()]
        return orders
