from scrapy import cmdline
import Config
import os
#from crawler.crawByUrlWord.spiders import BaiduSpider,BaikeSpider


def crawl():
    os.chdir(Config.CRAWL_PATH)
    os.system("scrapy crawl baidu -o {} -t csv -L ERROR".format(Config.BAIDU_PATH))
    os.system("scrapy crawl baike -o {} -t csv -L ERROR".format(Config.BAIKE_PATH))
    os.chdir(Config.WORK_PATH)

if __name__ == '__main__':
    #cmdline.execute("scrapy crawl baike -o {} -t csv -L ERROR".format(Config.BAIKE_PATH).split())
    crawl()