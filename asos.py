from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from asos_women.items import AsosWomenItem

class AsosSpider(BaseSpider):
    name = 'asos'
    allowed_domains = ['http://www.asos.com/women/accessories/cat/?cid=4174']
    start_urls = ['http://www.asos.com/women/accessories/cat/?cid=4174']

    

    def parse(self, response): # parse is the default callback method,if we change the name it wont work
      name=response.xpath('h1').extract
