import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from asoswomen.items import AsoswomenItem

class MySpider(CrawlSpider):
    name = 'asos'
    allowed_domains = ['www.asos.com']
    start_urls = ['http://www.asos.com/women/accessories/cat/?cid=4174&pgesize=36']

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//li[@class="next"]',)),callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//li[@class='product-container interactions']")
        #i = AsoswomenItem()
        items = []
        for title in titles:
            item = AsoswomenItem()
            item["name"] = title.select(".//span[@class='name']/text()").extract()
            item["price"] = title.select(".//span[@class='price']/text()").extract()
            items.append(item)
        return items
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['descri
