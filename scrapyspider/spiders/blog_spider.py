#-*- coding:UTF-8 -*-
from scrapy.spiders import Spider
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class BlogSpider(Spider):
    name = 'shitouboy'
    start_urls = ['https://blog.shitouboy.com']

    def parse(self, response):
        titles = response.xpath('//h2[@class="post-title"]/text()').extract()
        for title in titles:
            print title.strip()