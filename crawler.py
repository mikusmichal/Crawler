import abc
import datetime
import db


class Crawler:
    name = ''
    id = ''
    category = ''

    def crawl_site(self):

        for product, page in self.load_products():
            try:
                price = self.get_price(page)
                db.Database.insert_price(product, self.id, self.category, price, self.name, datetime.datetime.now())
                print('Product {} on page {} was successfully loaded'.format(product, page))
            except:
                db.Database.insert_price(product, None, self.category, None, self.name, datetime.datetime.now())
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

    @abc.abstractmethod
    def load_products(self):
        pass
