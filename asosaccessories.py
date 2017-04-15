import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from asos_women.items import AsosWomenItem

class AsosSpider(CrawlSpider):
    name = 'asos'
    allowed_domains = ['http://www.asos.com/women/accessories/cat/?cid=4174']
    start_urls = ['http://www.http://www.asos.com/women/accessories/cat/?cid=4174/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = AsosWomenItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
