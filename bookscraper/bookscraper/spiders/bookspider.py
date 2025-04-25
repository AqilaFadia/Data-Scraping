import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        
        products = response.css('.product_pod') 
        
        for product in products:
            
            yield{
                'name' : product.css('h3 a::attr(title)').get(),
                'price': product.css('.price_color::text').get(),
                'url' : product.css('h3 a::attr(href)').get()
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            