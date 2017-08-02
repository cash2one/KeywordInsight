# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawbyurlwordPipeline(object):
    count = 1
    def process_item(self, item, ampa):
        # sys.stderr.write(str(SscrawlerPipeline.count)+":"+item['url']+'\n')
        # SscrawlerPipeline.count += 1

        return item
