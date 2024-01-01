```python
import scrapy
from scraper.items import JobItem

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['nl.indeed.com']
    start_urls = ['https://nl.indeed.com/jobs']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        job_links = response.css('a.jobtitle.turnstileLink::attr(href)').getall()
        for link in job_links:
            yield response.follow(link, self.parse_job)

        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_job(self, response):
        item = JobItem()
        item['title'] = response.css('#jobsearch-JobComponent-title::text').get()
        item['company'] = response.css('#jobsearch-ViewJobLayout-company::text').get()
        item['location'] = response.css('#jobsearch-ViewJobLayout-location::text').get()
        item['description'] = response.css('#jobsearch-JobComponent-description::text').getall()
        yield item
```