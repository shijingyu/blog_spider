#-*- coding:UTF-8 -*-
from scrapy.spiders import Spider
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['https://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print title.strip()