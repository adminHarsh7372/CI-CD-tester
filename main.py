from scrapy.crawler import CrawlerProcess
from quotes_spider import QuotesSpider  # import your spider

# Configure the output feed
process = CrawlerProcess(settings={
    "FEEDS": {
        "output/quotes.csv": {"format": "csv"},  # output file
    },
})

# Run the spider
process.crawl(QuotesSpider)
process.start()
