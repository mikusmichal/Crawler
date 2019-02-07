import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect('input_db')
    cursor = db.cursor()
    database = cursor.execute('''INSERT INTO items(product, ID, category, shop, page) VALUES ('AMD RYZEN Threadripper 1900X', '2', 'CPU', 'czc', 'https://www.czc.cz/amd-ryzen-threadripper-1900x/221634/produkt')
        ''')
    db.commit()
    db.close()
