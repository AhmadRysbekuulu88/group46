import sqlite3


def fetch_products():



 def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    CHECK(lenth(product_title) <=200,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
     """)

    conn.commiit()
    conn.close()

    def add_products():
        products= [
            ('жидкое мыло с запахом ванили',50.0,10),
            ('детское мыло',30.0,15),
            ('шампунь',75.0,5),
            ('гель для душа',60.0,8),
            ('крем для рук',40.0,12),
            ('соль для ванны',20.0,20),
            ('губка для тела',15.0,25),
            ('средство для мытья посуды',45.0,18),
            ('талон для посещения бани',100.0,30),
            ('дезодорант',55.0,22),
            ('бальзам для губ',25.0,40),
            ('пена для ванны',35.0,16),
            ('шампунь против перхоти',80.0,9),
            ('маска для лица',65.0,11),
            ('скраб для тела',70.0,7),
]
        conn = sqlite3.connect('hw.db')
        cursor = conn.cursor()

        cursor.executemany('''
        INSERT INTO products (product_title,price,quantity)
        VAKUES (?,?,?)
        ''',products)

        conn.commit()
        conn.close()

        def update_quantity(id,new_quantity):
            conn.sqlite3.connect('hw.db.')
            cursor = conn.cursor()

            cursor.execute("""
            UPDATE produkts
            SET price=?
            WHERE id=?
            """,(new_quantity,id))

            conn.commit()
            conn.close()

            def update_quantity(id,new_quantity):
                conn=sqlite3.connect('hw.db')
                cursor=conn.cursor()

                cursor.execute("""
                UPDATE produkts
                SET price=?
                WHERE id=?
                """,(new_quantity,id))

                conn.commit()
                conn.close()

                def delete_product(id):
                    conn=sqlite3.connnnect('hw,db')
                    cursor=conn.cursor()

                    cursor.execute("""
                    DELETE FROM products
                    WHERE id=?
                    """,(id))

                    conn.commit()
                    conn.close()

                    def fetch_all_products():
                        cursor=conn.cursor()

                        cursor.execute('SELECT * FROM products')
                        products=cursor.fetchall()

                        for products in products:
                            print(products)

                            conn.close()

                            def fetch_products_below_price_and_above_quantity(price_limit,quanity_limit):
                                conn=sqlite3.connect('hw,db')
                                cursor=conn.cursor()

                                cursor.execute("""
                                SELECT * FROM products
                                WHERE price < ? AND quantity >?
                                """,(price_limit,quanity_limit))
                                products=cursor.fetchall()

                                for products in products:
                                    print(products)

                                    conn.close()

                                    def search_products_by_title(search_term):
                                        conn=sqlite3.connect('hw,db')
                                        cursor=conn.cursor()

                                        cursor("""
                                        SELECT * FROM products
                                        WHERE product_title LIKE ?
                                        """,('%'+ search_term + '%',))
                                        products=cursor.fetchall()
                                        for products in products:
                                            print(products)

                                            conn.close()

                                            if __name__ =='__main__':
                                                create_database()
                                                add_products()
                                                print('все товары')
                                                fetch_all_products()

















