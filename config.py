import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect('input_db')
    cursor = db.cursor()
    database = cursor.execute('''INSERT INTO items(product, ID, category, shop, page) VALUES ('Intel Core i7-7800X', '3', 'CPU', 'alza', 'https://www.alza.cz/intel-core-i7-7800x-d4977463.htm')
        ''')
    db.commit()
    db.close()
