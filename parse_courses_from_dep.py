from scrapy.crawler import CrawlerProcess
from course_parser.course_parser.spiders import deanza_spider
import scrapy


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(deanza_spider.CourseCatalogSpider)
process.start()  # the script will block here until the crawling is finished
