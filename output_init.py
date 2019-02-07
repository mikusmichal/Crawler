import sqlite3

if __name__ == "__main__":
    db = sqlite3.connect('prices_db')
    cursor = db.cursor()
    database = cursor.execute('''create table prices
                                    (
                                    product     text not null,
                                    ID          text,
                                    category    text,
                                    shop        text,
                                    page        text,
                                    price       int,
                                    time        text
                                    );
        ''')
    db.close()
