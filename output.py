import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect('prices_db')
    cursor = db.cursor()
    database = cursor.execute('''
        SELECT product, price, shop, time
        FROM prices
        ORDER BY product;
        ''')

    for row in database:
        print("PRODUCT = ", row[0])
        print("PRICE = ", row[1])
        print("SHOP = ", row[2])
        print("TIME = ", row[3], "\n")

    print("Operation done successfully")
    db.close()
