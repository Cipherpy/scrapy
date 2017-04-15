from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from asos_women.items import AsosWomenItem

class AsosSpider(BaseSpider):
    name = 'asos'
    allowed_domains = ['http://www.asos.com/women/accessories/cat/?cid=4174']
    start_urls = ['http://www.asos.com/women/accessories/cat/?cid=4174']

    

    def parse(self, response): # parse is the inbulit function we can not change the name
       pass
