```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.indeed_spider import IndeedSpider

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(IndeedSpider)
    process.start()

if __name__ == "__main__":
    main()
```