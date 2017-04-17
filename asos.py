# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

class ProductsSpider(Spider):
	name = "products"
        allowed_domains = ["asos.com"]
        start_urls = ['http://asos.com/women/']
	def __init__(self,product=None):
		self.product=product


    	def parse(self, response):
		if self.product:
			product_url=response.xpath('//a[text()[contains(.,"'+ self.product+ '")]]/@href').extract_first()
			yield Request(response.urljoin(product_url),callback=self.parse_product)
		else:
			self.logger.info('Scrapping all links available in the women category.')
			products=response.xpath('//*[@class="items"]/li/a/@href').extract()
			
			for product in products:
				#print product
				yield Request(response.urljoin(product),dont_filter=True,callback=self.parse_product)

	def parse_product(self,response):
		Product_typ=response.xpath('//*[@class="breadcrumb-current"]/text()').extract()
		Product_type1 = response.xpath("//li[@class='product-container interactions']")
		print Product_typ
		for product_type in Product_type1:

		        name = product_type.xpath(".//span[@class='name']/text()").extract()
			price =product_type.xpath(".//span[@class='price']/text()").extract()
			image=product_type.xpath(".//img/@src").extract()
			yield{
			
			'Image':image,
			'Product Type':Product_typ,
			'Name':name,
			'Price':price}

