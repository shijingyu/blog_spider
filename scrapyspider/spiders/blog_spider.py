# -*- coding:UTF-8 -*-
import scrapy

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from scrapyspider.items import TestSpiderItem


class Blog_spider(scrapy.Spider):
    name = "shitou_blog"
    start_urls = ['http://blog.shitouboy.com',
                  'http://blog.shitouboy.com/index2.html',
                  'http://blog.shitouboy.com/index3.html',
                  'http://blog.shitouboy.com/index4.html',
                  'http://blog.shitouboy.com/index5.html',
                  ]

    def parse(self, response):
        i = 0
        for sel in response.xpath('//div[@class="post-preview"]'):
            item = TestSpiderItem()
            item['title'] = sel.xpath('//h2[@class="post-title"]/text()')[i].extract()
            item['desc'] = sel.xpath('//p[@class="article-summary"]/text()')[i].extract()
            item['author'] = sel.xpath('//p[@class="post-meta"]/text()')[i].extract()
            i += 1
            yield item


