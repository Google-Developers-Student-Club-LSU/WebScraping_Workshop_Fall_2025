import scrapy

class BookScraper(scrapy.Spider):
    name = "moviescraper"

    start_urls = ["https://letterboxd.com/film/minions/reviews/by/activity/"]
    
    def parse(self, response):
        
        for review in response.css('.body'):
            
            yield{
                'username' : review.css('.displayname::text').get(),
                'text': review.css('.js-collapsible-text p::text').get(),
                'score': review.css('.-green::text').get()
                
            }
            next_page = response.css('.next::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)