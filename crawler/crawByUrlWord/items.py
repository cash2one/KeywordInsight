# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class CrawbyurlwordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BaiduItem(scrapy.Item):
    id = Field()
    title = Field()
    label = Field()
    old_word = Field()
    word = Field()
    baidu_summary = Field()
    url = Field()

class BaikeItem(scrapy.Item):
    old_word = Field()
    word = Field()
    baike_summary = Field()