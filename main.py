import threading
import sqlite3
from datetime import datetime
import yaml
from alza_crawler import AlzaCrawler
from czc_crawler import CzcCrawler


def crawl():
    start_time = datetime.now()
    czcCrawler = CzcCrawler()
    alzaCrawler = AlzaCrawler()
    czcCrawler.crawl_site()
    alzaCrawler.crawl_site()
    print('gathering done, proces finished after' + str(datetime.now() - start_time))


def do_stuff():
    print('done stuff, waiting')


def crawl_repeated():

    crawl()
    threading.Timer(60 * 5, crawl_repeated).start()  # twice per day
    # do_stuff()
    # threading.Timer(5, crawl_repeated).start()  # twice per day


if __name__ == '__main__':
    print('starting crawler')
    crawl_repeated()



