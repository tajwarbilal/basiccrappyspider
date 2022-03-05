# basiccrappyspider
Basic Scrappy Spider to scrape data from whiskey shop as well images-links-text and every concern information 
python3 -m venv venv
pip3 install scrapy
scrapy startproject whiskeyscraper

scrapy shell
fetch('https://www.whiskyshop.com/single-malt-scotch-whisky')

you can see the crawled with 200 response which means that you can fetch data acurately
response.css('product-item-info')
response.css('product-item-info').get()

products = response.css('product-item-info')
len(products)

products.css('a.product-item-link').get()
products.css('a.product-item-link::text').get()
products.css('a.product-item-link::text').getll()

products.css('span.price::text').get()
products.css('span.price::text').get().replace('pond', '')

products.css('a.product-item-link').attrib['href']

scrapy crawl whiskey
scrapy crawl whiskey -o whiskey.json

response.css('a.action.next').get()
response.css('a.action.next').attrib['href']
