from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from asoswomen.items import AsoswomenItem

class MySpider(BaseSpider):
    name = "asos"
    allowed_domains = ["asos.com"]
    start_urls = ["http://www.asos.com/women/accessories/cat/?cid=4174&pgesize=36"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//li[@class='product-container interactions']")
        items = []
        
        for title in titles:
            item = AsoswomenItem()
            item["name"] = title.select(".//span[@class='name']/text()").extract()
            item["price"] =title.select(".//span[@class='price']/text()").extract()
            item["image"]=title.select(".//img/@src").extract()
            items.append(item)
        return items
