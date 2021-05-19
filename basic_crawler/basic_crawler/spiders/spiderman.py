from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from basic_crawler.items import BasicCrawlerItem
from scrapy.http import Request

class MySpider(BaseSpider):
    name =  "basic_crawler"
    allowed_domains = ['']
    start_urls = ['']

    def parse(self, response):
        hxs = Selector(response)
        visited_links = []
        links = hxs.xpath('').extract()