from my_connection import get_connection

with get_connection('tms') as conn:
    with conn.cursor() as cursor:
        query = """
            UPDATE products
            SET discount = CASE WHEN id=1 THEN 15 ELSE 10 END
                        """

        cursor.execute(query)
