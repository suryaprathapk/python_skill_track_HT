import scrapy

class PostsSpider(scrapy.Spider):
    name = "card card-content"
    urls ='https://www.modeln.com/blog/'
    
   def parse(self, response):
        for post in response.css('div.card card-content'):
            yield {
                'title': post.css('.card-title ng-binding a::text')[0].get(),
                'date': post.css('.card-subtitle ng-binding a::text')[1].get(),
                }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)