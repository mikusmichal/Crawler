import re
import requests
import sqlite3
import db
from lxml import html
from crawler import Crawler


class AlzaCrawler(Crawler):

    def __init__(self):
        self.name = 'alza'

    def get_price(self, page):
        content = html.fromstring(requests.get(page).content)
        return self.price_text_to_int(content.cssselect(self.price_selector())[0].text)

    def price_text_to_int(self, price):
        return int(''.join(re.findall('\d+', price)))

    def price_selector(self):
        return '#prices span.price_withVat'

    def load_products(self):
        db_in = sqlite3.connect('input_db')
        cursor = db_in.cursor()
        return cursor.execute('SELECT product, page FROM items WHERE shop = "alza"')



