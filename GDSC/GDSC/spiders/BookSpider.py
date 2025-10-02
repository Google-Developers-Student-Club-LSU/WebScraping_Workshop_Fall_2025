import scrapy

class BookScraper(scrapy.Spider):
    name = "bookscraper"

    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self, response):
        
        for book in response.css('.col-lg-3'):
            yield {
                'title': book.css('.product_pod a::text').get(),
                'price': book.css('.price_color::text').get()
            }
            
            next_page = response.css('.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)