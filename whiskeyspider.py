from subprocess import call
from unicodedata import name
import scrapy

class WhiskeySpider(scrapy.Spider):
    name = 'whiskey'
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky']

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get(),
                    'link': products.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'Sold Out',
                    'link': products.css('a.product-item-link').attrib['href'],
                }
        
        nextpage = response.css('a.action.next').attrib['href']

        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)
