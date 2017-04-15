import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ["asos.com"]
    start_urls = ("http://www.asos.com/women/accessories/cat/?cid=4174&pgesize=36")

    #rules = (
        #Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)

    def parse(self, response):
        pass
