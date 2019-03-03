import threading
from datetime import datetime
from alza_crawler import AlzaCrawler
from czc_crawler import CzcCrawler


def crawl():
    start_time = datetime.now()
    czcCrawler = CzcCrawler()
    alzaCrawler = AlzaCrawler()
    czcCrawler.crawl_site()
    alzaCrawler.crawl_site()
    print('gathering done, process finished after' + str(datetime.now() - start_time))


def crawl_repeated():

    crawl()
    threading.Timer(60 * 60 * 12, crawl_repeated).start()  # twice per day


if __name__ == '__main__':
    print('starting crawler')
    crawl_repeated()
