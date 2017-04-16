from scrapy.spider import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from asoswomen.items import AsoswomenItem

from scrapy.linkextractors import LinkExtractor

from asoswomen.items import AsoswomenItem

class MySpider(CrawlSpider):
    name = "asos"
    allowed_domains = ["asos.com"]
    start_urls = ["http://www.asos.com/women/accessories/cat/?cid=4174&pgesize=36"]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="next"]',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//li[@class='product-container interactions']")
        items = []
        
        for title in titles:
            #item = AsoswomenItem()
            name = title.select(".//span[@class='name']/text()").extract()
            price =title.select(".//span[@class='price']/text()").extract()
            image=title.select(".//img/@src").extract()
            yield{'Image':image,'Name':name,'Price':price}
