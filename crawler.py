import abc
import datetime
import sqlite3
import requests
from lxml import html
import db
from lxml.cssselect import CSSSelector


class Crawler:
    products = {}
    name = ''
    ID = ''
    category = ''

    def crawl_site(self):

        db_in = sqlite3.connect('input_db')
        cursor = db_in.cursor()

        for product, page in cursor.execute('SELECT product, page FROM items'):
            try:
                price = self.get_price(page)
                db.Database.insert_price(product, price, self.name, self.ID, self.category, datetime.datetime.now())
                print('Product {} on page {} was successfully loaded'.format(product, page))
            except:
                db.Database.insert_price(product, None, self.name, self.ID, self.category, datetime.datetime.now())
                print('Product {} on page {} does not exist, skipping'.format(product, page))

    @abc.abstractmethod
    def get_price(self, page):
        pass

    @abc.abstractmethod
    def price_text_to_int(self, price):
        pass

    @abc.abstractmethod
    def price_selector(self):
        pass
