#coding: utf-8
import urllib.request

from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider
from scrapy.http import Request

import Config
from crawler.crawByUrlWord.items import BaiduItem


#百度搜索的爬虫，给一个词爬取搜索结果，和右边的推荐label


class BaiduSpider(CrawlSpider):
    name = "baidu"
    count = 0
    wordlst1= open(Config.WORDS_PATH, 'r').readlines()
    wordlst = [x.strip() for x in wordlst1]
    parselst = [urllib.parse.quote(x) for x in wordlst]
    start_urls = wordlst

    def make_requests_from_url(self, x):
        x_w = urllib.parse.quote(x)
        url = "https://www.baidu.com/s?wd={}".format(x_w)
        ret = Request(url, dont_filter=x)
        return ret

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        item = BaiduItem()
        item['word'] = response.request.dont_filter
        BaiduSpider.count += 1
        print(BaiduSpider.count,item['word'])
        item['url'] = response.request.url
        #right
        # 爬取右侧推荐label 例如"相关服饰","相关品牌"

        content_right_div = soup.find(id='content_right').find('div', attrs={'class': 'cr-content '})
        if content_right_div is not None:
            label = ''
            result_cr_content1 = content_right_div.find_all(
                'div', attrs={'class': 'cr-title c-clearfix'})
            result_cr_content2 = content_right_div.find_all(
                'div', attrs={'class': 'opr-recommends-merge-panel'})
            for result1,result2 in zip(result_cr_content1,result_cr_content2):
                label += result1.get_text().replace('展开', '').strip() + ':'
                for w in result2.find_all('div',attrs = {'class','c-gap-top-small'}):
                    label += w.get_text()+','
                label += '\n'
            item['label'] = label

        #left
        # 爬取左侧搜索结果
        content_left_div = soup.find(id='content_left')
        content = ''
        if content_left_div is not None:
            result_divs = content_left_div.find_all(
                'div', attrs={'class': 'result c-container '})
            for result_div in result_divs:
                title = ''
                abstract = ''
                title_h3 = result_div.find('h3', attrs={'class': 't'})  # title
                if title_h3 is not None:
                    title = ''
                    a_tag = title_h3.a
                    if a_tag is not None:
                        for s in a_tag.stripped_strings:
                            title += s.replace('\t', ' ').replace('\n', '')
                abstract_div = result_div.find('div', attrs={'class': 'c-abstract'})  # abstract
                if abstract_div is not None:
                    for s in abstract_div.stripped_strings:
                        abstract += s.replace('\t', ' ').replace('\n', '')
                content += title+' '+abstract+'\n'

        item['baidu_summary'] = content

        return item