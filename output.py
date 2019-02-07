import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect('prices_db')
    cursor = db.cursor()
    database = cursor.execute('''
        SELECT product, ID, category, price, shop, time
        FROM prices;
        ''')

    for row in database:
        print("PRODUCT = ", row[0])
        print("ID = ", row[1])
        print("CATEGORY = ", row[2])
        print("PRICE = ", row[3])
        print("SHOP = ", row[4])
        print("TIME = ", row[5], "\n")

    print("Operation done successfully")
    db.close()
