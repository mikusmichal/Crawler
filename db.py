import sqlite3


class Database:

    @staticmethod
    def insert_price(product, ID, category, shop, price, time):
        db = sqlite3.connect('prices_db')
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO prices(product, ID, category, price, shop, time) VALUES (?, ?, ?, ?, ?, ?)
        ''', (product, ID, category, shop, price, str(time)))
        db.commit()
        db.close()
