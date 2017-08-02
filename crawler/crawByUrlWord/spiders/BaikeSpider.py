#coding: utf-8
import urllib.request

from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider
from scrapy.http import Request

import Config
from crawler.crawByUrlWord.items import BaikeItem


#百科词条的爬虫，给一个词爬取summary，暂未对多义词做处理


class BaikeSpider(CrawlSpider):
    name = "baike"
    count = 0
    wordlst1= open(Config.WORDS_PATH, 'r').readlines()
    wordlst = [x.strip() for x in wordlst1]
    parselst = [urllib.parse.quote(x) for x in wordlst]
    start_urls = wordlst

    def make_requests_from_url(self, x):
        x_w = urllib.parse.quote(x)
        url = "http://baike.baidu.com/item/{}".format(x_w)
        ret = Request(url, dont_filter=x)
        return ret

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        item = BaikeItem()
        item['old_word'] = response.request.dont_filter
        BaikeSpider.count += 1
        print(BaikeSpider.count,item['old_word'])
        html_cont = response.body.decode('utf-8')
        if html_cont.find('您所访问的页面不存在...') != -1:
            return item

        # 处理苹果类别的多义词 网页没内容只有多义词选项
        if html_cont.find('多义词') != -1 and html_cont.find('lemma-summary') == -1:
            #node = soup.find('div',class_='lemmaWgt-subLemmaListTitle')
            #muti_means = node.find_all('div',class_="para")
            return item

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        item['word'] = title_node.get_text()
        cont_node = soup.find('div',class_='lemma-summary')
        item['baike_summary'] = cont_node.get_text()
        return item