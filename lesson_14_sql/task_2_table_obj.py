from dataclasses import dataclass


@dataclass
class Customer:
    '''class Customer'''
    name: str
    age: int
    address: str
    balance: int

    def add_new_customer(self, cursor):
        query = """INSERT INTO customers(name, age, address, balance)
                    VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (self.name, self.age, self.address, self.balance))

    @staticmethod
    def get_id_by_name(name, cursor) -> int:
        query = """SELECT id FROM customers WHERE name = %s;"""
        cursor.execute(query, (name,))
        return cursor.fetchone()[0]


@dataclass
class Product:
    '''class Customer'''
    name: str
    price: int
    count: int
    description: str
    discount: int
    category: str

    @classmethod
    def get_product_by_id(cls, name, cursor):
        query = """SELECT pr.name, pr.price, pr.count_to_stock,
                        pr.description, pr.discount, cat.name
                    FROM products AS pr
                    INNER JOIN category AS cat ON cat.id = pr.category_id
                    WHERE pr.id = %s"""
        product_id = cls.get_id_by_name(name, cursor)
        cursor.execute(query, (product_id,))
        product_fields = cursor.fetchone()
        return cls(*product_fields)

    @staticmethod
    def get_id_by_name(name, cursor) -> int:
        query = """SELECT id FROM products WHERE name = %s;"""
        cursor.execute(query, (name,))
        return cursor.fetchone()[0]


@dataclass
class Order:
    '''class Customer'''
    product_name: str
    category_name: str
    product_price: int
    product_count: int
    product_description: str

    @staticmethod
    def add_new_order(product_count, customer_id, product_id, cursor):
        query = """INSERT INTO orders (product_count, customer_id, product_id)
                    VALUES (%s, %s, %s)"""
        cursor.execute(query, (product_count, customer_id, product_id))

    @classmethod
    def get_orders_by_cumstomer_name(cls, customer_name, cursor):
        query = """SELECT pr.name, cat.name, pr.price, o.product_count,
                           pr.description
                    FROM orders AS o
                        INNER JOIN customers AS cus on cus.id = o.customer_id
                        INNER JOIN products AS pr on pr.id = o.product_id
                        INNER JOIN category AS cat on cat.id = pr.category_id
                    WHERE cus.name = %s"""
        cursor.execute(query, (customer_name,))
        order_fields = cursor.fetchone()
        return cls(*order_fields)


from my_connection import get_connection

c = Customer('Tom', 30, 'some address 4', 900)
# o = Order(23, 3, 1)
with get_connection('tms') as conn:
    with conn.cursor() as cursor:
        # c.add_new_customer(cursor)
        # o.add_new_order(cursor)
        # conn.commit()
        res = Order.get_orders_by_cumstomer_name('Alex', cursor)
        print(res)
